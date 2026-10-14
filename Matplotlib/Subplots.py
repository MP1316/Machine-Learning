import matplotlib.pyplot as plt
#fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))
# fig, ax = plt.subplots(1,2, figsize = (10,5))


# x = [1,2,3,4]
# y = [10,20,15,25]

# ax[0].plot(x,y)
# ax[0].set_title('Line Plot')

# ax[1].bar(x,y)
# ax[1].set_title('Bar chart')
# plt.tight_layout()
# plt.show()

fig, ax = plt.subplots(2,2)
ax[0,0].plot([1,2,3], [2,4,6])
ax[0,0].set_title("Plot 1")

ax[0,1].plot([1,2,3], [3,2,5])
ax[0,1].set_title("Plot 2")

ax[1,0].plot(["A", "B", "C"], [5,3,8])
ax[1,0].set_title("Plot 3")

ax[1,1].plot([1,2,3], [4,1,6])
ax[1,1].set_title("Plot 4")

plt.tight_layout()
plt.show()


