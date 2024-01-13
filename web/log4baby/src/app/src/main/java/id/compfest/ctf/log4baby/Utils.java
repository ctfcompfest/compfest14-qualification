package id.compfest.ctf.log4baby;

import javax.servlet.http.HttpServletRequest;

public class Utils {
	public String getBrowserName(HttpServletRequest request) {
		return request.getHeader("User-Agent");
	}
}
