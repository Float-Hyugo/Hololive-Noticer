import discord
from discord.ext import commands
import json

class manage():
  def __init__(self,bot):
    self.bot = bot
    
  def read_json(fp:str):
    with open(f'{fp}.josn',mode='r') as f:
      res = json.load(f)
      
    return res
      
  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    
    streamer = self.read_json('streamer')
    
    main_ctg = await guild.create_category(name="HoloNoticer")
    set_channel = await main_ctg.create_text_channel(name='setting')
    exp_channel = await main_ctg.create_text_channel(name='使い方')
    
    #json config
    user_info = self.read_json('notice')
    
    guild_info = {'set_ch':set_channel.id,'exp_ch':exp_channel.id,'noticer':[]}
    
    user_info['users'][guild.id] = guild_info
    
    #send msg
    await set_channel.send('settingチャンネルの初期設定を完了してください。')
    
    embed = discord.Embed(title='通知設定',description='通知をするライバーを設定します。')
    
    streamer_name = list()
    streamer_img = list()
    streamer_url = list()
    
    
    for k,v in streamer['streamer'].items():
      streamer_name.append(k)
      streamer_img.append(v['img'])
      streamer_url.append(v['url'])
      
    pages = len(streamer_name)
    now_page = 1
    list_idx = 0
    
    embed.add_field(name='名前',value=f'[{streamer_name[list_idx]}]({streamer_url[list_idx]})')
    embed.set_thumbnail(url=f'{streamer_url[list_idx]}')
    
    msg = await set_channel.send(embed=embed)
      
    while True:
      
      
    
    
    
    
