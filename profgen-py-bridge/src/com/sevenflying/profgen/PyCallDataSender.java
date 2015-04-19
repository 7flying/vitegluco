package com.sevenflying.profgen;

import java.util.Map;

/** Interface that a python object must implement to receive data
 * from the profile generator.
 * @author flying
 */
public interface PyCallDataSender {
	
	/** Sends results to a Python method.
	 * @param results - map of results
	 */
	public void sendResults(Map<String, String> results);
	
}
