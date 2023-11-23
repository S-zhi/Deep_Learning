import dataset
from matplotlib import pyplot as plt 
xs,ys=dataset.get_beans(150)
print(xs)
print(ys)

# 配置图像

plt.title("Size-Toxicity Function",fontsize = 12 )
plt.xlabel("Bean Size")
plt.ylabel("Toxicity")

plt.scatter(xs,ys)


# y = 0.5*x
w=0.5 
for i in range(100) : 
	x = xs[i]
	y = ys[i]
	y_pre = w * x * 0.01
	e  = y - y_pre

	alpha = 0.05 
	w = w + alpha*e*x
y_pre=w*xs 
# 在这里面是相关的广播方式
print(y_pre)
plt.plot(xs,y_pre)
plt.show()
