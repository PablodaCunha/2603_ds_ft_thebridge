import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

def main():
    print("Hello from proyecto-uv!")
    print("Vamos a jugar con numpy")

    x = [1,2,3]
    y = [4,5,6]
    z = [7,8,9]

    concatenado = np.concatenate([[x], [y], [z]], axis = 0)
    print("concatenado", concatenado)



    cubo = np.ones((3,3,3))
    plane = np.zeros((3,3))

    cubo_ext = np.concatenate([cubo, plane[np.newaxis,:]])
    print(cubo_ext)

    print("ahora jugamos con ydata profiling")
    df = pd.DataFrame(np.random.rand(100,5), columns=["a", "b", "c", "d", "e"])
    profile = ProfileReport(df, title= "YData Profiling Report")
    profile.to_file("your_report.html")

print("the value of __name__ is", __name__)

if __name__ == "__main__":
    main()