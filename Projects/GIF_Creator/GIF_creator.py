import imageio.v3 as iio

filenames = ["GIF_Creator/Assets/team-pic1.png", "GIF_Creator/Assets/team-pic2.png"]   
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('GIF_Creator/Output/team.gif', images, duration = 500, loop = 0)