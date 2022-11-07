# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 03:08:10 2022

@author: Björn
"""

cmap = [(0.8857501584075443, 0.8500092494306783, 0.8879736506427196, 1.0),
 (0.8697047485350982, 0.8515240300479789, 0.8805388339000336, 1.0),
 (0.8441261828674842, 0.8440648271103739, 0.8671697332269007, 1.0),
 (0.8095999819094809, 0.8293189667350546, 0.8506444160105037, 1.0),
 (0.7675110850441786, 0.8098007598713145, 0.8325281663805967, 1.0),
 (0.7209728066553678, 0.7872399592345264, 0.8151307392087926, 1.0),
 (0.6731442255942621, 0.7626890873389048, 0.8002762854580953, 1.0),
 (0.6266240202260459, 0.7367017540369944, 0.7884690131633456, 1.0),
 (0.5830148703693241, 0.7095888767699747, 0.7792578182047659, 1.0),
 (0.5430593242401823, 0.6815376725306588, 0.7719407969783508, 1.0),
 (0.5070896957645166, 0.6526417240314645, 0.7659044566083585, 1.0),
 (0.47533752394906287, 0.6229275728383581, 0.7606508557181775, 1.0),
 (0.4480247093358917, 0.5923833145214658, 0.7557417647410792, 1.0),
 (0.42532423665011354, 0.560981049599503, 0.7507516498900512, 1.0),
 (0.4072701869421907, 0.5286918801105741, 0.7452494263758127, 1.0),
 (0.39367135736822567, 0.4954965577745118, 0.738794102296364, 1.0),
 (0.38407269378943537, 0.46139018782416635, 0.7309466543290268, 1.0),
 (0.3777794975351373, 0.4263845142616835, 0.7212763999353023, 1.0),
 (0.3739349933047578, 0.3905082752937583, 0.7093613429347845, 1.0),
 (0.3716113323440048, 0.3538121372967869, 0.6947714991938089, 1.0),
 (0.3698798032902536, 0.31638410101153364, 0.6770375543809057, 1.0),
 (0.3678384369653108, 0.2783869718129776, 0.655605668384537, 1.0),
 (0.3645930889012501, 0.24013747024823828, 0.629786801550261, 1.0),
 (0.35920088560930186, 0.20226037920758122, 0.5987265295935138, 1.0),
 (0.3506030444193101, 0.1659512998472086, 0.5614796470399323, 1.0),
 (0.3376473209067111, 0.13324562282438077, 0.5174080757397947, 1.0),
 (0.31946262395497965, 0.1066887988239266, 0.46713728801395243, 1.0),
 (0.2963100038890529, 0.08771325096046395, 0.41346259134143476, 1.0),
 (0.2700863774911405, 0.07548367558427554, 0.36056376228111864, 1.0),
 (0.24367372557466271, 0.06841985515092269, 0.3121652405088837, 1.0),
 (0.22001251100779617, 0.0658579189189076, 0.2709027999432586, 1.0),
 (0.2015613376412984, 0.06798327102620025, 0.23852974228695395, 1.0),
 (0.18488035509396164, 0.07942573027972388, 0.21307651648984993, 1.0),
 (0.20290365333558247, 0.06943524858045896, 0.21833167885096033, 1.0),
 (0.2257539681670791, 0.06738213230014747, 0.22728984778098055, 1.0),
 (0.2558213554748177, 0.06953231029187984, 0.24112190491594204, 1.0),
 (0.29128515387578635, 0.0748990498474667, 0.25755101595750435, 1.0),
 (0.3302917447118144, 0.08246763389003825, 0.27430929404579435, 1.0),
 (0.3712250843130934, 0.09167999748026273, 0.2894586539763317, 1.0),
 (0.41277985630360303, 0.1026734006932461, 0.3015422643746897, 1.0),
 (0.4538300508699989, 0.11622183788331528, 0.3097044124984492, 1.0),
 (0.49335504375145617, 0.13328091630401023, 0.31386561956734976, 1.0),
 (0.5305442048985645, 0.15436183633886777, 0.3148129978918713, 1.0),
 (0.564973435290177, 0.17923664950367169, 0.3139136046337036, 1.0),
 (0.5965991810912237, 0.207212956082026, 0.3125852303112123, 1.0),
 (0.6255741650043496, 0.23756535071152696, 0.3119669831491227, 1.0),
 (0.652074172902773, 0.269746505252367, 0.3129056060581917, 1.0),
 (0.6762189792440975, 0.30339762792450425, 0.3160724937230589, 1.0),
 (0.6980608153581771, 0.3382897632604862, 0.3220747885521809, 1.0),
 (0.7176044490813385, 0.3742627271068619, 0.3315213862095893, 1.0),
 (0.7348413359856494, 0.4111778700451951, 0.3450416947080907, 1.0),
 (0.7497942054717047, 0.4488833348154881, 0.3632633755836028, 1.0),
 (0.7625733355405261, 0.48718906673415824, 0.38675335037837993, 1.0),
 (0.7734402182988989, 0.5258533209345156, 0.41592679539764366, 1.0),
 (0.7828622526444091, 0.5645853311116688, 0.45093985823706345, 1.0),
 (0.7915283284347561, 0.603066705931472, 0.49159667021646397, 1.0),
 (0.8002941538975398, 0.6409821330674986, 0.5373053518514104, 1.0),
 (0.8100280946652069, 0.6780367267397182, 0.5871062690808275, 1.0),
 (0.8213947205565636, 0.7139109141951604, 0.6397176669767276, 1.0),
 (0.8345656905566583, 0.7481379479992134, 0.6935569764986385, 1.0),
 (0.8489224556311764, 0.7799202140765015, 0.7466371929366437, 1.0),
 (0.8626560105112757, 0.8080552380426153, 0.796282666437655, 1.0),
 (0.8733517136091627, 0.8309671525127262, 0.8374885100119709, 1.0),
 (0.8821154248940161, 0.8455700725455935, 0.8667376504623333, 1.0)]

import taichi as ti
import numpy as np
from PIL import Image

ti.init(arch=ti.gpu)

win_size_s = [1920, 1080]
center = [-0.908445250432262, -0.2676926298264956]
pixels_s = ti.field(dtype=ti.float64, shape=(win_size_s[0], win_size_s[1]))
scale=0.0000236000184180249
itr_lim_s = 25000

###############################################################################

@ti.func
def complex_sqr_fancy(z: ti.float64):
    return ti.Vector([z[0]**2 - z[1]**2, z[1] * z[0] * 2])


@ti.kernel
def paint_fancy(s: ti.float64, c1: ti.float64, c2: ti.float64):
    for i, j in pixels_s:
        
        x_min = c1 - s
        x_max = c1 + s
        y_min = c2 - s*(win_size_s[1]/win_size_s[0])
        y_max = c2 + s*(win_size_s[1]/win_size_s[0])
        x = x_min + (x_max-x_min)*(i/win_size_s[0])
        y = y_min + (y_max-y_min)*(j/win_size_s[1])
        
        z = ti.Vector([0, 0], dt=ti.float64)
        c = ti.Vector([x, y], dt=ti.float64)
        
        itr = 0
        while z.norm() < 16 and itr < itr_lim_s:
            z = complex_sqr_fancy(z) + c
            itr += 1
            
        pixels_s[i, j] = itr

###############################################################################

def save_frame(d, q):
    print('Saving frame ' + str(saved_frames)+"/"+str(max_frames))
    paint_fancy(d[0], d[1], d[2])
    image = np.zeros((win_size_s[1], win_size_s[0], 3), dtype=np.uint8)
    itr = pixels_s.to_numpy(dtype=np.float64)
    itr_mod = np.mod(itr+q, 64)
    for i in range(win_size_s[1]):
        for j in range(win_size_s[0]):
            if itr[j, i] == itr_lim_s:
                image[i,j,:]=0
            else:
                image[i,j,0] = cmap[int(itr_mod[j,i])][0]*255.0
                image[i,j,1] = cmap[int(itr_mod[j,i])][1]*255.0
                image[i,j,2] = cmap[int(itr_mod[j,i])][2]*255.0
    image = Image.fromarray(image, 'RGB')
    name = "frame" + str(saved_frames) + ".png"
    image.save(name)

###############################################################################

if __name__=="__main__":
    i = 0
    saved_frames = 0
    max_frames=64
    for i in range(max_frames):
        saved_frames = i
        save_frame([scale, center[0], center[1]], i)
        i=i+1
    print('Done!')

    