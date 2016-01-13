from nyaa import nyaa
import guessit
import sys

NYAA_USERS = {
'hoshisora.moe':[158741,],
'puya.se': [239789,],
}

def main():

    for fansub, users in NYAA_USERS.items():
        for user in users:
            offset = 1
            while True:
                results = nyaa.search(user=user,offset=offset)
                if not results:
                    break
                offset +=1
                for res in results:
                    data = guessit.guessit(res.title)
                    try:
                        fansub,data["release_group"], data["title"]
                    except KeyError:
                        print data


if __name__=="__main__":
    main()
