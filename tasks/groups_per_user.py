def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for users, group in group_dictionary.items():
		# Now go through the users in the group
		for user in group:
			# Now add the group to the the list of
			# groups for this user, creating the entry
			# in the dictionary if necessary
			user_groups[users]=group


	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))