# This code operates the Alternative Voting System to elect the PJCC Chairperson/Secretary
# Run using python3 pjcc_election.py, then follow the instructions on the screen
#NB This is python3 code
# Tom Galligan (PJCC Chairperson 2016-18)

#TODO put in placeholders
# add max no of sig figs to print

import numpy as np

#change as appropriate
#members = ['Tom Galligan','Jack Bara','Joe Clarke','Teneeka Mai','Maris Serzans',
#			'Josh Long','Matt Davies', 'Ishraq Irteza','Dougal Main','Nicole Jacobus',
#			'Josh Form','Aakash Lakshmanan','Toby Adkins']
#
#candidates = ['A','B','C','D','E','F','G','RON']

#for testing:
members = ['Tom', 'Joe', 'Jeremy', 'Seb']
candidates = ['Obama', 'Bush', 'Clinton', 'Trump']


n_members = len(members)
n_candidates = len(candidates)
print('Number of PJCC members: ', n_members)
print('Number of candidates for election: ', n_candidates)

data = np.zeros((n_members, n_candidates),dtype=int)

#first we input the votes
#this assumes you enter the candidate preferences with comma separation.
# e.g. if Tom ranks candidate A 3rd, B 1st, C 2nd and RON 4th, you would enter 3 1 2 4
for i in range(n_members):
	usr_input = input('Enter candidate preferences for '+members[i]+': ').split(' ')
	usr_input_arr = np.array(usr_input, dtype=int) # convert to array of integers
	
	#check dimensions
	while(len(usr_input) != n_candidates):
		print("You seem to have entered the wrong number of preferences. Try again.")
		usr_input = input('Enter candidate preferences for %s: ' % members[i]).split(',')
		usr_input_arr = np.array(usr_input, dtype=int) # convert to array of integers
		
	data[i,:] = usr_input_arr

print('-----------')


# some error handling
no_errors = True
for i in range(n_members):
	data_temp = data[i,:] # row we're considering in this iteration

	if len(np.unique(data_temp)) != n_candidates: # someone's put the same rank twice
		no_errors = False
		rep_idx = [np.argwhere(i==data_temp) for i in np.unique(data_temp)] # this picks out repeated values
		for arr in rep_idx:
			if len(arr)>1: # repeated rank
				arr = arr.reshape(len(arr))
				print('\nWARNING: The following candidates were both ranked at ' + str(data_temp[arr[0]]) + ' by '+members[i]+':\n')
				for k in arr:
					print(candidates[k])

	if np.max(data_temp)>n_candidates: # someone's ranked one of the candidates too low
		no_errors = False
		print('\n'+members[i]+' has ranked the following candidates too low:\n')
		for k in range(n_candidates):
			if data_temp[k] > n_candidates:
				print(candidates[k])
		print('\n---------------\n')
if no_errors == True:
	print('\nNo errors found')

#--------------------------------------------------------------------------

# We can now proceed with the election.
votes = np.zeros(n_candidates,dtype=int) # number of votes each candidate has

round = 1


#----FIRST RUNOFF-----
#distribute 1st prefs to each candidate

print('---------ROUND 1---------\n')
for i in range(n_candidates):
	votes[i] = np.sum(data[:,i]==1)
	print(candidates[i]+': '+str(votes[i])+'('+str(100.*float(votes[i])/n_members)+'%)')
# eliminate all candidates with 0 1st prefs. 
print('\nCandidates eliminated in round 1 with zero votes:')
for i in range(len(votes)):
	if votes[i]==0:
		print(candidates[i])
#votes = votes[votes>0] # trim off the eliminated candidates



#-----REMAINING RUNOFFS--------

while np.max(votes) <= n_members/2.0:
	round += 1 
	print("\n\n---------ROUND %s--------- \n" % str(round))
	for i in range(n_candidates):
		if votes[i] != 0:
			print(candidates[i]+': '+str(votes[i])+'('+str(100.*float(votes[i])/n_members)+'%)')
		else:
			print('Candidate %s eliminated' % candidates[i])
	# find candidates with lowest non-zero number of votes
	# first see if there's only one:

	if len(votes[votes==np.min(votes[votes!=0])]) > 1: # more that one lowest non-zero vote count
		lowest_candidates = np.where(votes==np.min(votes[votes!=0]))[0]

		#sum their non-1st votes, largest sum is eliminated
		other_votes = np.zeros(len(lowest_candidates))
		for i in range(len(lowest_candidates)):
			other_votes[i] = np.sum(data[:,lowest_candidates[i]])

		eliminated = int(lowest_candidates[np.argmax(other_votes)]) # index of eliminated candidate
		print('Candidate '+candidates[eliminated]+' eliminated at round '+str(round)+' after a tie breaker.\n')

	else:
		eliminated = np.argmin(votes)
		print('Candidate '+candidates[int(eliminated)]+' eliminated at round'+str(round)+'.\n')

	votes[eliminated] = 0
	
	#check if there's only one candidate left. If so, declare them the winner.
	if len(votes[votes!=0]) == 1:
		break

	# find out who voted for voted for the person just eliminated
	sad_voters = np.where(data[:,eliminated] == np.min(data[:,eliminated]))[0]

	#for each sad voter, find the person they liked most who's still in the running, and add
	# the sad voter's votes to this person's total. 
	for voter in sad_voters:
		voter_prefs = data[voter,:]
		# get index of next best candidate still in the race
		next_best = int(np.where(voter_prefs == np.min(voter_prefs[votes!=0]))[0])

		votes[next_best] += 1 # increase this candidate's votes by 1 
		print("%s has put %s as their next favourite that's still in the running" %(members[voter], candidates[next_best]))
		print("Increasing candidate %s's vote count by 1" % candidates[next_best])


print('Candidate ' + candidates[np.argmax(votes)] + ' elected with ' + str(np.max(votes)) + ' votes.')

print('----ELECTION COMPLETE----')










			







