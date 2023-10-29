import pygame as p, os, moviepy.editor as m, glob as g
def e(v: str, i: str) -> None:
 if not os.path.isfile(i+"/frame%04d.png"):
  c=m.VideoFileClip(v)
  c.write_images_sequence(i+"/frame%04d.png")
  c.audio.write_audiofile(i+"/audio.wav")
def play_intro_video(i, n, s):
 c=p.time.Clock();f=sorted(g.glob(i+"/frame*.png"));a=i+"/audio.wav";p.mixer.music.load(a);p.mixer.music.play()
 for m in f:
  if n == True:
   e=p.image.load(m).convert();s.blit(e,(0,0));p.display.flip();c.tick(60)
   for v in p.event.get():
    if v.type==p.VIDEORESIZE:s=p.display.set_mode((v.w,v.h),p.RESIZABLE)
    if v.type==p.QUIT:p.quit();quit()
    if v.type==p.KEYDOWN:n=False
 p.mixer.music.stop()
