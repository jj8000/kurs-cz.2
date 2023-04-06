import matplotlib.pyplot as plt

x_list = []
y_list = []

with open('reg_punkty.txt', 'r') as f:
    data = f.readlines()

for i in data:
    i = i.strip().split(';')
    x_list.append(int(i[0]))
    y_list.append(int(i[1]))

plt.scatter(x_list, y_list)

xy_list = [x_list[i]*y_list[i] for i in range(len(x_list))]
x2_list = [x**2 for x in x_list]

n = len(x_list)

print((xy_list))

b = (n*sum(xy_list)-sum(x_list)*sum(y_list))/(n*sum(x2_list)-(sum(x_list))**2)
# print(b)
a = (sum(y_list)/n) - b * (sum(x_list)/n)
# print(a)
def linia_regresji(a, b, x):
    return b * x + a


# zamienił a z b

plot_y = [linia_regresji(a, b, x) for x in x_list]

plt.plot(x_list, plot_y, color="r", label=f"{round(b, 2)} x + {round(a, 2)}")
plt.grid()
plt.legend()

plt.show()