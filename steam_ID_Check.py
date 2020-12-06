import requests

from mykey import KEY

def is_S_parent(sid):

    res = (requests.get("http://api.steampowered.com/IPlayerService/IsPlayingSharedGame/v0001/?key="+KEY+"&format=json&steamid="+sid+"&appid_playing=4000"))

    new_sid = (res.json()['response']['lender_steamid'])
    new_sid = sid

    if new_sid != 0:
        res = requests.get("https://steamidfinder.com/lookup/" + new_sid)

        dec_pos = res.text.find("steamID64 (Dec):")
        dec_pos = res.text.find(">", dec_pos)+1
        steamID = (res.text[dec_pos:res.text.find("<", dec_pos)])
        steamLink = "http://steamcommunity.com/profiles/"+steamID

        return "\nInitial SteamID: "+sid+"\nNew SteamID: "+new_sid+"\n"+steamLink

        # return str(str(res.text[dec_pos: res.text.find("<", dec_pos)]) == sid) +"\ninitial sid: "+sid+"\nnew sid: "+new_sid
