import numpy as np




estudiantes = np.array([[2.4,4.0,5.0],
                        [3.5,5.0,5.0],
                        [3.5,3.0,5.0],
                        [3.0,2.0,5.0]])



print(estudiantes[0]) 

promedio=estudiantes[1:,2].astype(float).mean()
print(promedio)
