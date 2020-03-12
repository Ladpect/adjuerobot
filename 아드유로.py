import discord, asyncio, random, datetime
import os

client = discord.Client() #긴거 대신함

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("아듀로 도움 하면 도와줌"))
    print("준비 되었다")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.author.bot: #채팅친 놈이 봇이면 구문 종료
        return None

    if message.content == "아듀로 안녕":
        await message.channel.send("안녕")
        #channel을 author로 바꾸면 DM으로 감

    if message.content == "아듀로 정체":
        await message.channel.send("우주에서 온 이상한 사람")

    if message.content == "아듀로":
        await message.author.send("why?")

    if message.content == "아듀로 뭐라도 해봐":
        await message.channel.send("나는 인공지능이 아니란다^^")

    if message.content == "아듀로 고마워":
        await message.channel.send("당신의 칭찬에 찬사를!")
        
    if message.content == "아듀로 도움":
        embed = discord.Embed(title="아드유로 봇 명령어들", description="이용법은 '아듀로 (명령어)'야. 적다고? 곧 추가할거야 아드유로가 일을 해야할텐데...", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="대화", value="고마워, 뭐라도 해봐, 정체, 안녕, 따라해 (할말), 주사위 (숫자), 잘했어, 시간", inline=False)
        embed.add_field(name="이미지", value="김두한, 물리치료사, 심영, 햄스터, 프로필, 둘기이마트", inline=False)
        embed.add_field(name="기타", value="DM (유저ID) (할말), 추가 예정", inline=False)
        embed.add_field(name="밀크초코 온라인", value="밀초 도움", inline=False)
        embed.set_footer(text="자주 봐두면 좋아!")
        await message.channel.send("도움이 필요하신가요?", embed=embed)
        
    if message.content == "아듀로 도움pro":
        embed = discord.Embed(title="아드유로 봇 명령어들", description="이용법은 '아듀로 (명령어)'야. 적다고? 곧 추가할거야 아드유로가 일을 해야할텐데...", color=0x4641D9)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.add_field(name="관리", value="뮤트죄수(임명/해제) (유저ID)", inline=False)
        embed.add_field(name="대화", value="고마워, 뭐라도 해봐, 정체, 안녕, 따라해 (할말), 주사위 (숫자), 잘했어, 시간", inline=False)
        embed.add_field(name="이미지", value="김두한, 물리치료사, 심영, 햄스터, 둘기이마트, ", inline=False)
        embed.add_field(name="기타", value="채널확성기 (채널ID) (할말), DM (유저ID) (할말)", inline=False)
        embed.add_field(name="밀크초코 온라인", value="밀초 도움", inline=False)
        embed.set_footer(text="자주 봐두면 좋아!")
        await message.channel.send("도움이 필요하신가요?", embed=embed)
   
    if message.content == "아듀로 김두한":
        embed = discord.Embed(title="김두한.", description="1972의 사나이", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685873878723067915/1541313521858.jpg")
        embed.set_footer(text="다함께 폭사하자.")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)

    if message.content == "아듀로 물리치료사":
        embed = discord.Embed(title="마사지사양반.", description="자자 이리로 왓", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874384295952427/1518347904432.gif")
        embed.set_footer(text="그래도 의사니까 안심하자.")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)

    if message.content == "아듀로 심영":
        embed = discord.Embed(title="심영이.", description="국민 고자", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874314138222640/JPEG_20180922_092147.jpg")
        embed.set_footer(text="폭8이다!.")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)

    if message.content == "아듀로 햄스터":
        embed = discord.Embed(title="햄스터?", description="정체불명", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/685874094411087988/hamster.jpg")
        embed.set_footer(text="나는 그냥 햄스터다 인간들아")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)
        
    if message.content == "아듀로 둘기이마트":
        embed = discord.Embed(title="둘기는 이마트를 좋아해", description="난나난나나나나", color=0x4641D9)
        embed.set_image(url="https://cdn.discordapp.com/attachments/685873675555176492/686185101700104215/KakaoTalk_20200308_200354653.jpg")
        embed.set_footer(text="이마트는 둘기를 싫어합니다")
        await message.channel.send("아듀로 이미지 서비스", embed=embed)
        
    if message.content.startswith("아듀로 채널확성기"):
        channel = message.content[10:29] #채널 아이디는 18자, ?번째 글자와 ?번째 글자 사이에 그거 
        msg = message.content[29:] #할말 보내는거
        await client.get_channel(int(channel)).send(msg) #채널 그게 정수값으로 해서 그채널 보내게 함
        
    if message.content.startswith("아듀로 DM"):
        author = message.guild.get_member(int(message.content[7:26])) #유저 아이디
        msg = message.content[26:] #유저에게 할말
        await author.send(msg)
        
    if message.content.startswith("아듀로 뮤트죄수임명"):
        author = message.guild.get_member(int(message.content[11:30])) #유저 아이디
        role = discord.utils.get(message.guild.roles, name="죄수") #죄수 임명 변수
        await author.add_roles(role)#죄수 임명

    if message.content.startswith("아듀로 뮤트죄수해제"):
        author = message.guild.get_member(int(message.content[11:30])) #유저 아이디
        role = discord.utils.get(message.guild.roles, name="죄수") #죄수 변수 찾아라
        await author.remove_roles(role)#죄수 해제
        
    if message.content.startswith("아듀로 따라해"):
        msg = message.content[8:] #할말 보내는거
        await message.channel.send(msg) #할말 보내는거
        
    if message.content.startswith("아듀로 주사위"):
        num = message.content[8:]
        op = random.randint(0, int(num))
        await message.channel.send(op)

    if message.content == "아듀로 잘했어":
        await message.channel.send("yeah! dude, THX")
        
    if message.content == "아듀로 프로필":
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x4641D9)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉넴", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    
    if message.content == "아듀로 시간":
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        await message.channel.send("지금의 시간은 " + str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 입니다")

    if message.content == "아듀로 밀초 도움":
        embed = discord.Embed(title="아듀로 봇의 밀초 정보 저장소", description="영웅들과 총 정보 등등 많은 정보를 제공합니다", color=0x4641D9)
        embed.add_field(name="캐릭터", value="어썰트, 메딕, 바머, 리콘, 고스트, 쉴드, (추가 예정)", inline=False)
        embed.add_field(name="총기", value="(유저들이 주로 쓰는 총으로 추가 예정(캐릭터 기입 완료시))", inline=False)
        embed.add_field(name="유의사항 1", value="1.정보가 맞지 않을 수 있습니다.", inline=False)
        embed.add_field(name="유의사항 2", value="2.원뚝여부에 총기 옆에 '(S)'가 있다면 리콘, 에어, 스위니의 스킬사용중 스나뎀 10퍼 추가일시에 그렇다는 겁니다.", inline=False)
        embed.add_field(name="원뚝여부 (최대뎀 기준 (원래뎀)/(스킬추가뎀), (샷건최대뎀)", value="에땁 168/184, 알디 173/190 스피라 184/202 신스나 193/212 클샷 220 신샷 230", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/685873793121779712/7648feb42b9bd245.jpg")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("아듀로 밀초 어썰트"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 어썰트", description="굴러라 굴러", color=0x4641D9)
        embed.add_field(name="체력", value="200", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="스피라(S) 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="1.6초동안 구른다. 이때 적군과 부딫히면 0.4초마다 40뎀이 들어간다. 추가적으론 구르기 상태에선 피격데미지 절반감소, 모든 판정이 몸샷이 된다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634145853308962/cdb73b014dbd173a.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("아듀로 밀초 메딕"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 메딕", description="의사양반! 이쪽에...", color=0x4641D9)
        embed.add_field(name="체력", value="210", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="X", inline=True)
        embed.add_field(name="원뚝여부", value="신스나(S) 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="아군 1명의 체력을 90회복한다. 시체가 터지지 않은 팀원을 90체력으로 부활, 잠시동안 무적상태 부여, 부활한 아군 데스기록제거를 할 수 있다. 그리고 스킬 시전시 자신의 체력 30회복한다.", inline=False)
        embed.add_field(name="배틀로얄", value="스킬 사용불가로 인해 회복템 사용속도가 감소한다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634142053269570/741a1317414241ce.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("아듀로 밀초 바머"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 바머", description="다함께 폭사하자.", color=0x4641D9)
        embed.add_field(name="체력", value="225", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="100/13", inline=True)
        embed.add_field(name="원뚝여부", value="X", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 앞으로 돌진후 폭파하며 최대 250 데미지를 입힌다. (이 스킬은 벽뒤에 숨어도 맞는다.)", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634143408029721/f605c923f31b3f55.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("아듀로 밀초 리콘"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 리콘", description="버프를 굉장히 많이 먹는 아이.", color=0x4641D9)
        embed.add_field(name="체력", value="150", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="70/32", inline=True)
        embed.add_field(name="원뚝여부", value="클샷 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 지형투시와 인비스킬, 크리미 지뢰(스킬)을 감지할 수 있다.(아군 전체적용, 크리미 지뢰(스킬)파괴 가능) 그리고 스킬쓰는 동안에는 스나뎀이 10% 상승한다.", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634139909849114/3f5b28ad7369b2e4.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("아듀로 밀초 쉴드"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 쉴드", description="방패에 의존하는 은근 대처하기 어렵고 단단한 아이", color=0x4641D9)
        embed.add_field(name="체력", value="170", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="135/15", inline=True)
        embed.add_field(name="원뚝여부", value="X", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰면 8초간 방패를 들며 총알을 막는다.(단, 적군의 스킬은 막을 수 없다), 방패를 들면 이동속도가 느려지며 총을 바꿀 수 없다.", inline=False)
        embed.add_field(name="부가사항", value="스킬을 공중에서 쓰면 잠깐 공중에서 멈추었다가 아주 빠르게 떨어진다. 이것을 응용하면 잔기술을 만들 수 있다.", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634144347422745/7c0b2093df6cb7fb.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

    if message.content.startswith("아듀로 밀초 고스트"):
        embed = discord.Embed(title="밀초 캐릭터 정보 : 고스트", description="뒤치 전문가", color=0x4641D9)
        embed.add_field(name="체력", value="140", inline=True)
        embed.add_field(name="배리어/배리어 충전량", value="30/20", inline=True)
        embed.add_field(name="원뚝여부", value="알디 이상의 데미지", inline=True)
        embed.add_field(name="스킬", value="스킬을 쓰고 특정 위치에 에임을 갖다대면 그곳으로 순간이동한다. (단, 무조건 바닥에 에임을 갖다대야한다. 벽 or 천장에 할 시 스킬이 발동이 안된다.)", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/685873675555176492/687634071039639587/82eb70e95996fb6b.png")
        embed.set_footer(text="아듀로 봇의 존재이유.")
        await message.channel.send("아듀로 밀초 정보 서비스", embed=embed)

        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
