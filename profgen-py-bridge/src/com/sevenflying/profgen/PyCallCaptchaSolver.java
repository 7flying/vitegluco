package com.sevenflying.profgen;

/** Interface that a python object must implement to communicate with
 * the profile generator to sove captchas.
 * @author flying
 */
public interface PyCallCaptchaSolver {
		
	/** Requests a captcha resolution to Python.
	 * @param captchaUrl - the captcha image url
	 * @return the image's text
	 */
	public String solveCaptcha(String captchaUrl);
}
