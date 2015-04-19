package com.sevenflying.profgen;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.deustotech.computing.generators.ProfileGenerator;
import com.deustotech.computing.generators.model.BaseGenerator;
import com.deustotech.computing.generators.model.Generator;
import com.deustotech.computing.generators.model.GmailGenerator;
import com.deustotech.computing.generators.model.MailComGenerator;
import com.deustotech.computing.generators.model.MailGenerator;
import com.deustotech.computing.generators.model.TwitterGenerator;
import com.deustotech.computing.generators.model.factories.GeneratorFactory;
import com.deustotech.computing.generators.model.factories.MailMapperFactory;
import com.deustotech.computing.generators.model.interfaces.MailMapeable;

public class Profgen {
	
	public void generateTwitter(PyCallDataSender dataSender, String uuid,
			String name, String lastname, String username, String email,
			List<String> toFollow)
	{
		Map<String, String> params = new ProfileGenerator(Generator.TWITTER)
		.getRequiredParams();
		params.put(TwitterGenerator.fullNameParam, name + " " + lastname);
		params.put(TwitterGenerator.emailParam, email);
		params.put(TwitterGenerator.usernameParam, username);
		if (toFollow != null && toFollow.size() > 0) {
			int i = 0;
			for (String user : toFollow) {
				params.put(TwitterGenerator.toFollowPrefix
						+ Integer.toString(i), user);
				i++;
			}
		}
		BaseGenerator base = GeneratorFactory.createGenerator(
				Generator.TWITTER, params, null);
		Map<String, String> results = null;
		try {
			results = base.generateProfile();
			results.put("uuid", uuid);
		} catch(Exception e) {
			results = new HashMap<String, String>();
			results.put("message", "Generation failed");
			results.put("uuid", uuid);
		}
		base.logout();
		base.closeBrowser();
		results.put("type", "TWITTER");
		dataSender.sendResults(results);
	}

	public void generateTwitterEmail(PyCallCaptchaSolver capatchaSolver,
			PyCallDataSender dataSender, String uuid, String name,
			String lastname, String username, String email,
			String emailType, String sex, String bday, String bmonth,
			String byear, List<String> toFollow)
	{
		ProfileGenerator temp = emailType.equals("GMAIL")
		? new ProfileGenerator(Generator.TWITTER, MailGenerator.GMAIL)
		: new ProfileGenerator(Generator.TWITTER, MailGenerator.MAILCOM);
		Map<String, String> params = temp.getRequiredParams();
		params.put(TwitterGenerator.fullNameParam, name + " " + lastname);
		params.put(TwitterGenerator.emailParam, null);
		params.put(TwitterGenerator.usernameParam, username);
		if (toFollow != null && toFollow.size() > 0) {
			int i = 0;
			for (String user : toFollow) {
				params.put(TwitterGenerator.toFollowPrefix
						+ Integer.toString(i), user);
				i++;
			}
		}
		Map<String, String> extraParams = temp.getRequiredExtraParams();
		extraParams.put(MailComGenerator.birthYear, byear);
		extraParams.put(MailComGenerator.birthMonth, bmonth);
		extraParams.put(MailComGenerator.birthDay, bday);
		extraParams.put(MailComGenerator.sex, sex);
		if (emailType.equals("GMAIL"))
			extraParams.put(GmailGenerator.emailUsernameParam, email);
		else
			extraParams.put(MailComGenerator.account, email);
		temp.quit();
		// Generation
		Exception ex = null;
		BaseGenerator base = null;
		try {
			// Generate mapper
			MailMapeable mailMapper = MailMapperFactory.createMailMapper(
				emailType.equals("GMAIL") ? MailGenerator.GMAIL
						: MailGenerator.MAILCOM,
						Generator.TWITTER, false);
			Map<String, String> generatedParams = mailMapper.mapMailParams(
					emailType.equals("GMAIL") ? MailGenerator.GMAIL
						: MailGenerator.MAILCOM, params, extraParams);
			// Generate mail
			base = GeneratorFactory.createEmailGenerator(
					emailType.equals("GMAIL") ? MailGenerator.GMAIL
							: MailGenerator.MAILCOM,
					generatedParams, new GetCaptchaExtender(capatchaSolver));
			Map<String, String> mailData = base.generateProfile();
			System.out.println("mail com generated");
			base.closeBrowser();
			mailData.put("uuid", uuid);
			mailData.put("type", emailType);
			dataSender.sendResults(mailData);
			email = mailData.get(BaseGenerator.UNAME);
		} catch(Exception e) {
			ex = e;
			Map<String, String> results = new HashMap<String, String>();
			results.put("message", "Generation failed");
			results.put("uuid", uuid);
			results.put("type", emailType);
			dataSender.sendResults(results);
		}
		if (base != null) {
			base.logout();
			base.closeBrowser();
		}
		if (ex == null) {
			generateTwitter(dataSender, uuid, name, lastname, username,
					email, toFollow);
		}
	}
}
