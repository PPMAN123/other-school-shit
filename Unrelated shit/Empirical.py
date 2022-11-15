import math

mapping = {
'H':1.007,
'He':4.002,
'Li':6.941,
'Be':9.012,
'B':10.811,
'C':12.011,
'N':14.007,
'O':15.999,
'F':18.998,
'Ne':20.18,
'Na':22.99,
'Mg':24.305,
'Al':26.982,
'Si':28.086,
'P':30.974,
'S':32.065,
'Cl':35.453,
'Ar':39.948,
'K':39.098,
'Ca':40.078,
'Sc':44.956,
'Ti':47.867,
'V':50.942,
'Cr':51.996,
'Mn':54.938,
'Fe':55.845,
'Co':58.933,
'Ni':58.693,
'Cu':63.546,
'Zn':65.38,
'Ga':69.723,
'Ge':72.64,
'As':74.922,
'Se':78.96,
'Br':79.904,
'Kr':83.798,
'Rb':85.468,
'Sr':87.62,
'Y':88.906,
'Zr':91.22,
'Nb':92.906,
'Mo':95.96,
'Tc':98,
'Ru':101.07,
'Rh':102.90,
'Pd':106.42,
'Ag':107.868,
'Cd':112.41,
'In':114.818,
'Sn':118.71,
'Sb':121.76,
'Te':127.6,
'I':126.904,
'Xe':131.293,
'Cs':132.905,
'Ba':137.327,
'La':138.90,
'Ce':140.116,
'Pr':140,
'Nd':144.24,
'Pm':145,
'Sm':150.36,
'Eu':151.964,
'Gd':157.2,
'Tb':158.925,
'Dy':162.5,
'Ho':164.93,
'Er':167.259,
'Tm':168.934,
'Yb':173.05,
'Lu':174.967,
'Hf':178.49,
'Ta':180.948,
'W':183.84,
'Re':186.207,
'Os':190.23,
'Ir':192.217,
'Pt':195.084,
'Au':196.967,
'Hg':200.59,
'Tl':204.383,
'Pb':207.2,
'Bi':208.98,
'Po':210,
'At':210,
'Rn':222,
'Fr':223,
'Ra':226,
'Ac':227,
'Th':232.038,
'Pa':231,
'U':238.029,
'Np':237,
'Pu':244,
'Am':243,
'Cm':247,
'Bk':247,
'Cf':251,
'Es':252,
'Fm':257,
'Md':258,
'No':259,
'Lr':262,
}

numOfElements = int(input('Number of individual elements: '))
elements = []
percents = []
for i in range(numOfElements):
  element, percentage = input('Separate element with space: ').split(' ')
  percentage = float(percentage)/100

  elements.append(element)
  percents.append(percentage)

