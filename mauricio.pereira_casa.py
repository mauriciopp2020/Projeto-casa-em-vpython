from vpython import *
#Web VPython 3.2

terreno = box(pos=vec(0,0,0),size=vec(90,0.1,80));
alicesse = box(pos=vec(0,0.8,0),size=vec(65,1.5,70),texture=textures.wood);
#==============================1 andar=================================================
casa = box(pos=vec(5,9,-10),size=vec(55,15,50),texture=textures.metal);
casa = box(pos=vec(22.5,9,21.5),size=vec(20,15,13),texture=textures.metal);

coluna = box(pos=vec(-31,10,32),size=vec(1,17,1),texture=textures.metal);
coluna = box(pos=vec(-31,10,-1),size=vec(1,17,1),texture=textures.metal);
coluna = box(pos=vec(-31,10,-32),size=vec(1,17,1),texture=textures.metal);

teto = box(pos=vec(0,16.3,0),size=vec(65,0.1,70),texture=textures.wood);
tetocima = box(pos=vec(0,17.9,0),size=vec(65,3,70));
teto = box(pos=vec(0,34.5,0),size=vec(65,0.1,70),texture=textures.wood);
tetocima = box(pos=vec(0,36,0),size=vec(65,3,70));
teto = box(pos=vec(0,19.5,0),size=vec(65,0.1,70),texture=textures.wood);
teto = box(pos=vec(0,37.5,0),size=vec(65,0.1,70),texture=textures.wood);

Porta= box(pos=vec(1,7.3,15),size=vec(9,12,0.1));
janelaFrente= box(pos=vec(22.5,9,28),size=vec(9,9,0.1));
janelaLado= box(pos=vec(-22.5,9,0),size=vec(0.1,9,9));
janelaLado= box(pos=vec(-22.5,9,-25),size=vec(0.1,9,9));
janelaLado= box(pos=vec(32.5,9,-25),size=vec(0.1,9,9));
janelaLado= box(pos=vec(32.5,9,0),size=vec(0.1,9,9));

#==============================2 andar=================================================
casa = box(pos=vec(0,27,-10),size=vec(65,15,50),texture=textures.metal);
coluna = box(pos=vec(-31,27,32),size=vec(1,17,1),texture=textures.metal);
coluna = box(pos=vec(31,27,32),size=vec(1,17,1),texture=textures.metal);
coluna = box(pos=vec(0,30,32),size=vec(1,11,1),texture=textures.metal);
protecao = box(pos=vec(31,21,20),size=vec(1,7,23),texture=textures.wood);
protecao = box(pos=vec(-31,21,20),size=vec(1,7,23),texture=textures.wood);
protecao = box(pos=vec(0,21,32),size=vec(61,7,1),texture=textures.wood);


Porta= box(pos=vec(1,25,15),size=vec(9,12,0.1));
janelaFrente= box(pos=vec(22.5,27,15),size=vec(9,9,0.1));
janelaFrente= box(pos=vec(-22.5,27,15),size=vec(9,9,0.1));

janelaLado= box(pos=vec(32.5,28,-25),size=vec(0.1,9,9));
janelaLado= box(pos=vec(32.5,28,0),size=vec(0.1,9,9));
janelaLado= box(pos=vec(-32.5,28,-25),size=vec(0.1,9,9));
janelaLado= box(pos=vec(-32.5,28,0),size=vec(0.1,9,9));
#===============================================================================
