import matplotlib.pyplot as plt

# Datos del archivo para ESRGAN
archivos_esrgan = ["j1.jpg", "j2.jpg", "j3.jpg", "j4.jpg", "j5.jpg", "j6.jpg", "j7.jpg", "j8.jpg", "j9.jpg", "j10.jpg",
            "j11.jpg", "j12.jpg", "j13.jpg", "j14.jpg", "j15.jpg", "j16.jpg", "j17.jpg", "j18.jpg", "j19.jpg", "j20.jpg",
            "j21.jpg", "j22.jpg", "j23.jpg", "j24.jpg", "j25.jpg", "j26.jpg", "j27.jpg", "j28.jpg", "j29.jpg", "j30.jpg",
            "j31.jpg", "j32.jpg", "j33.jpg", "j34.jpg", "j35.jpg", "j36.jpg", "j37.jpg", "j38.jpg", "j39.jpg", "j40.jpg",
            "j41.jpg", "j42.jpg", "j43.jpg", "j44.jpg", "j45.jpg", "j46.jpg", "j47.jpg", "j48.jpg", "j49.jpg", "j50.jpg"]

mse_valores_esrgan = [168.79982747395835, 168.71403645833334, 170.58071614583332, 171.695478515625, 87.81362955729166, 164.62811197916668,
               164.8555859375, 165.074169921875, 164.57677083333334, 164.79554036458333, 164.97322591145834, 165.088701171875,
               161.10023763020834, 161.062744140625, 161.21270833333332, 161.2563671875, 161.18728841145833, 161.61843098958335,
               161.43359700520833, 161.076484375, 155.26835611979166, 154.87127604166668, 155.36737955729166, 155.57311848958332,
               155.1884375, 155.68781901041666, 155.95739908854168, 155.79101888020833, 155.137216796875, 154.87404296875,
               155.03389973958335, 155.36737955729166, 155.52641276041666, 155.57311848958332, 155.12824544270833, 155.5364453125,
               89.718212890625, 89.15159830729166, 89.17642903645833, 89.54251627604167, 61.628108723958334, 60.498798828125,
               157.175283203125, 155.85953776041666, 183.258623046875, 183.01025065104167, 183.09540690104166, 183.21161783854166,
               183.25017252604167, 155.767890625]

psnr_valores_esrgan = [25.857083624594715, 25.859291448892726, 25.811504274995887, 25.7832150240804, 28.69518432864588,
                25.965763633150427, 25.95976693582054, 25.954012387741763, 25.967118241035966, 25.961349060629964,
                25.956668941232294, 25.953630101164634, 26.059841798440235, 26.060852666642248, 26.05681086789046,
                26.05563489158724, 26.057495714784693, 26.045894745986573, 26.050864372008714, 26.060482186586142,
                26.219974058660824, 26.231094841891927, 26.217205199253947, 26.211458035625693, 26.222210003697736,
                26.20825726100076, 26.200743770482504, 26.205379432386323, 26.223643650489127, 26.2310172516208,
                26.22653689406569, 26.217205199253947, 26.21276205820144, 26.211458035625693, 26.223894803781068,
                26.212481916622487, 28.601997466421118, 28.62951227267755, 28.628302833097127, 28.61051066337069,
                30.233015207918164, 30.313336088186773, 26.16696109320197, 26.203469769693534, 25.50015941791763,
                25.50604945036359, 25.50402911064042, 25.50127351125642, 25.500359686757676, 26.206024220471335]

# Datos del archivo para Result
archivos_result = ["j1.jpg", "j2.jpg", "j3.jpg", "j4.jpg", "j5.jpg", "j6.jpg", "j7.jpg", "j8.jpg", "j9.jpg", "j10.jpg",
            "j11.jpg", "j12.jpg", "j13.jpg", "j14.jpg", "j15.jpg", "j16.jpg", "j17.jpg", "j18.jpg", "j19.jpg", "j20.jpg",
            "j21.jpg", "j22.jpg", "j23.jpg", "j24.jpg", "j25.jpg", "j26.jpg", "j27.jpg", "j28.jpg", "j29.jpg", "j30.jpg",
            "j31.jpg", "j32.jpg", "j33.jpg", "j34.jpg", "j35.jpg", "j36.jpg", "j37.jpg", "j38.jpg", "j39.jpg", "j40.jpg",
            "j41.jpg", "j42.jpg", "j43.jpg", "j44.jpg", "j45.jpg", "j46.jpg", "j47.jpg", "j48.jpg", "j49.jpg", "j50.jpg"]

mse_valores_result = [3.148271484375, 3.363844401041667, 3.475436197916667, 3.1318359375, 2.899469401041667, 3.7851302083333334,
               3.600244140625, 3.5537109375, 3.6993196614583335, 3.670234375, 3.5560677083333334, 3.3020833333333335,
               6.405950520833334, 6.693577473958333, 6.41966796875, 5.99349609375, 5.899889322916667, 5.960485026041667,
               6.2789518229166665, 6.258681640625, 7.264781901041666, 7.508912760416667, 6.925299479166667, 7.4021484375,
               6.938460286458334, 7.350478515625, 7.225260416666667, 6.947291666666667, 6.793824869791667, 7.764700520833333,
               7.437545572916667, 6.925299479166667, 7.609560546875, 7.4021484375, 7.087734375, 6.147415364583333,
               4.57798828125, 3.972994791666667, 3.9418229166666667, 3.9393359375, 3.694794921875, 3.570296223958333,
               5.9409798177083335, 6.154638671875, 6.079296875, 5.838916015625, 6.198232421875, 5.987760416666666,
               5.2863997395833335, 5.37283203125]

psnr_valores_result = [43.15008185121724, 42.862444621284425, 42.72071040730371, 43.17281357579282, 43.507618309976365,
                42.34999537061405, 42.567484086197524, 42.62398261921487, 42.449585001637175, 42.48386562414424,
                42.62110339425864, 42.94292331689728, 40.064967809909405, 39.874220664284486, 40.05567794336237,
                40.354001342541494, 40.4223649615753, 40.377987595902894, 40.151932100474525, 40.165974999419085,
                39.51857780168612, 39.37503302203859, 39.726418019996885, 39.43722570984151, 39.718172539986114,
                39.46764748323733, 39.54226856085257, 39.71264828718056, 39.80966013368254, 39.22955650920229,
                39.416507210213084, 39.726418019996885, 39.3172078393676, 39.43722570984151, 39.62572927614392,
                40.24387802627136, 41.52405684236457, 42.13962365143509, 42.17383250828584, 42.17657342845895,
                42.454900228108784, 42.6037611027576, 40.392222838443274, 40.238777995253656, 40.29227008727726,
                40.46748132270663, 40.20812503445892, 40.35815945917207, 40.899203609576944, 40.82877097265811]

# Graficar MSE y PSNR en un solo gráfico para ESRGAN y Result
plt.figure(figsize=(15, 5))

# Gráfico para MSE
plt.subplot(1, 2, 1)
plt.plot(mse_valores_esrgan, marker='o', linestyle='-', color='b', label='ESRGAN')
plt.plot(mse_valores_result, marker='o', linestyle='-', color='r', label='Result')
plt.title('MSE')
plt.xlabel('Imagenes')
plt.ylabel('Valor de MSE')
plt.legend()

# Gráfico para PSNR
plt.subplot(1, 2, 2)
plt.plot(psnr_valores_esrgan, marker='o', linestyle='-', color='b', label='ESRGAN')
plt.plot(psnr_valores_result, marker='o', linestyle='-', color='r', label='Result')
plt.title('PSNR')
plt.xlabel('Imagenes')
plt.ylabel('Valor de PSNR en decibelios (dB)')
plt.legend()

plt.tight_layout()
plt.show()