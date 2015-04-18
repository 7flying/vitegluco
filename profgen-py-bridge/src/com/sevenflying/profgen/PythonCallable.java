package com.sevenflying.profgen;

import java.util.Map;

/** Interface that a python object must implement to comunicate with
 * the profile generator.
 * @author flying
 */
public interface PythonCallable {
	
	/** Sends results to a Python method.
	 * @param results - map of results
	 */
	public void sendResults(Map<String, String> results);
	
	/** Requests a captcha resolution to Python.
	 * @param captchaUrl - the captcha image url
	 * @return the image's text
	 */
	public String solveCaptcha(String captchaUrl);
}
