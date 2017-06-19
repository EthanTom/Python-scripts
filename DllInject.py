from immlib import *

DESC = "DllInjector : Inject Dll's Into Any Process."

def usage(imm)
	imm.log("!DllInject Location of the DLL [ To Inject ]")

def main(args):
	imm = Debugger()
	imm.log("\n DllInjector : Inject Dll's         /")
	imm.log("                                   _ /_")
	imm.log("							       / D /")
    imm.log("							      / L /")
	imm.log("                                /_L_/")
	imm.log("								 //")
	imm.log("							   /_/")
	imm.log("\nCreated By - @Ice3man")

	if not args:
		imm.log("\n[!] Not Enough Arguments. ")
		usage(imm)

	dll_path = args[0]

	try:
		injectDll(self, dll_path)
		imm.log("[*] Dll Successfully Injected Into Target Process.")

	except:
		imm.log("[!] Some Error Occured. Couldn't Inject.")

return "[*] Process Completed. See Logs for Details."
