package com.sevenflying.profgen;

import com.deustotech.computing.generators.model.GetCaptcha;

/** Extends the required class in profgens to solve captchas.
 * @author flying
 */
public class GetCaptchaExtender extends GetCaptcha {

	private PyCallCaptchaSolver pycall;
	
	public GetCaptchaExtender(PyCallCaptchaSolver pycall) {
		super();
		this.pycall = pycall;
	}

	public String solveCaptcha(String url) {
		return pycall.solveCaptcha(url);
	}

}
