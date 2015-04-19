package com.sevenflying.profgen;

import py4j.GatewayServer;


/** Entry point for the profile generator service
 * @author flying
 */
public class ProfgenEntryPoint {

	private Profgen profgen;
	
	public ProfgenEntryPoint() {
		this.profgen = new Profgen();
	}
	
	public Profgen getProfgen() {
		return profgen;
	}

	public static void main(String[] args) {
		GatewayServer gateway = new GatewayServer(new ProfgenEntryPoint());
		gateway.start();
	}
}
