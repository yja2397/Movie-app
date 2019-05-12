package Jython;

import org.python.util.PythonInterpreter;

public class main {
	private static PythonInterpreter interpreter;
	
	public static void main(String[] args) {
		System.setProperty("python.cachedir.skip", "true");
		interpreter = new PythonInterpreter();
		interpreter.execfile("test_2.py");
		interpreter.exec("print(sum(5,8))");
	}
}
