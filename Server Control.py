OS is Debian, Jessie

#Things we need variables / global variables for
gamelist=['ARK','7D2D','FOREST','RUST','L4D2'] #Names of games servers exist for. There are also matching roles in discord the same name as these.
#Map names for games that will support multiple?
ark_map=['TheIsland','TheCenter','Ragnarok','ScorchedEarth_P']
7D2D_map=['map1','map2'] #Insert game names here for check.
current_game
approved_roles=['ADMIN','MOD'] #add the name of the roles that can stop any server
start_user #To store user who initiated server
server_running=0
current_server='$game from gamelist'
server_PID

#command to start server from bot
!start Rust
#starts Rust for example
#But bot checks user roles
#Bot also checks if server_running=1, will not start a server if one is already active
if server_running=1
	message #- 'current_server' is currently running
elif ('RUST' in message.author.roles) #Possibly a if statement reading in a message with the !start removed, rather than an if for every game
	#start rust using popen to capture PID to server_PID
	#save userid to start_user so only that user can stop server
	#changes server_running to 1
	#Deletes chats and outputs "Rust server is running"
else
	return

#if the game has multiple maps, send the request for map name
if message(!start ARK)
	#Check user roles for permission
	#Check if server_running=0
	#Send new message asking for map with $map 'ark_map'
	#waits for message with map name
	#inserts value in place of ark_map (below) in start argument
	start ShooterGameServer.exe ark_map?SessionName=potato?ServerPassword=potato?ServerAdminPassword=****?Port=?QueryPort=?listen?MaxPlayers=1 exit
	#capture PID via popen and store as server_PID
	#set server_running to 1
	#Deletes chats and outputs "Ark server is running"

#Stop sequence
if message(!stop)
	#check if ADMIN or MOD is in message.author.roles
	#else check if userid matches start_user
	#killPID command sent with server_PID to shell
	#set server_running to 0
	#Deletes chat and outputs "No server is running"
else
	#Direct Message User 'you do not have authority to stop this server'



