def check_password(password, min_length=8):
	if len(password)>=min_length:
		return True, "Strong password"
	return False, "Password too short"
is_valid,status = check_password("samyu")
print("Valid:", is_valid, "| status_message:", status)
