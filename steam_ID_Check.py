import requests

from mykey import KEY

#
 # @brief returns a steamID and link to steam profile
 # @date 12/5/2020
 # @param sid is the steam id the function takes in from the discord chat
 # @returns steamID after being checked with the steamAPI and the link to the related steam profile
#

def is_S_parent(sid):
    #after generating a steam api key, someone can use this link to check if a user is using a family shared account by checking what the link returns
    res = (requests.get("http://api.steampowered.com/IPlayerService/IsPlayingSharedGame/v0001/?key="+KEY+"&format=json&steamid="+sid+"&appid_playing=4000"))

    #new_sid = sid
    new_sid = (res.json()['response']['lender_steamid'])


    if new_sid != 0:
        res = requests.get("https://steamidfinder.com/lookup/" + new_sid)

        dec_pos = res.text.find("steamID64 (Dec):")
        dec_pos = res.text.find(">", dec_pos)+1
        steamID = (res.text[dec_pos:res.text.find("<", dec_pos)])
        steamLink = "http://steamcommunity.com/profiles/"+steamID

        return "\nInitial SteamID: "+sid+"\nNew SteamID: "+new_sid+"\n"+steamLink

        # return str(str(res.text[dec_pos: res.text.find("<", dec_pos)]) == sid) +"\ninitial sid: "+sid+"\nnew sid: "+new_sid
