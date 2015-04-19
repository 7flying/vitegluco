package com.sevenflying.profgen;

import py4j.GatewayServer;


/** Entry point for the profile generator service
 * @author flying
 */
public class ProfgenEntryPoint {
	
	public ProfgenEntryPoint() {}
	
	public Profgen getProfgen() {
		return new Profgen();
	}

	public static void main(String[] args) {
		GatewayServer gateway = new GatewayServer(new ProfgenEntryPoint());
		gateway.start();
	}
}
