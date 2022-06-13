#!/usr/bin/env python3


# ---THIS TOOL OR PROGRAM---
# ---USING INDONESIAN LANGUAGE.---


def md2_hash_tool_version_2(created_by="ruben leonardo sigalingging."):
	# Langkah pertama: Import module python yaitu OS
	import os
	from os import system
	# Clear screen
	system("clear")
	from pyfiglet import figlet_format
	from sys import version_info
	from time import sleep
	import Crypto.Hash
	from Crypto.Hash import MD2
	import json
	import urllib
	import requests
	import datetime
	import math
	import wikipedia
	from urllib import request
	tema = figlet_format("MD2", font="slant")
	print(tema)
	print("\033[91m[\033[94m!\033[91m] \033[94mCode By: \033[91mRuben Leonardo Sigalingging.")
	print("\033[91m[\033[94m!\033[91m] \033[94mCreated On: \033[91mMonday, June 13, 2022, 11:55 am.")
	print("\033[91m[\033[94m!\033[91m] \033[94mUsing: \033[91mPython Programming Language Version 3.8.10.")
	print("\n")
	print("\033[0m\033[91m---\033[0m\033[94m\033[3mMD2 HASH TOOL\033[0m\033[91m---")
	plaintext = input("\033[91m[\033[94m!\033[91m] \033[94mInput Plaintext: \033[91m\033[3m")
	hash_function_md2 = MD2.new()
	hash_function_md2.update(plaintext.encode("ascii"))
	print("")
	print("The MD2 Hash Value Is ", hash_function_md2.hexdigest())
	print("\n")


	ask = "Y"
	question = input("\033[0m\033[91m[\033[0m\033[94m!\033[0m\033[91m] \033[0m\033[94mDo You Want To Save \033[0m\033[91mThis Hash Result?\n\033[0m\033[91m[\033[0m\033[94m!\033[0m\033[91m] \033[0m\033[94mY/n ~> \033[0m\033[91m")
	if question == "Y" or question == "y":
		save_result_md2_hash = open("MD2HashResult.txt","w")
		save_result_md2_hash.write("Plaintext: ")
		save_result_md2_hash.write(plaintext)
		save_result_md2_hash.write("\n")
		save_result_md2_hash.write("MD2 Hash Value: ")
		save_result_md2_hash.write(hash_function_md2.hexdigest())
		save_result_md2_hash.write("\n")
		print("")
		print("\033[0m\033[91m[\033[0m\033[94m!\033[0m\033[91m] \033[0m\033[94mFile Saving \033[0m\033[91mSuccess!")
		print("\033[0m\033[91m[\033[0m\033[94m!\033[0m\033[91m] \033[0m\033[94mFile Saved As ~> \033[0m\033[91m"+str(save_result_md2_hash))
		print("")
	elif question != "Y" or question != "y":
		from os import system
		system("exit")
md2_hash_tool_version_2()