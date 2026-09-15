import matplotlib.pyplot as plt

x_data = [0, 1, 2, 3, 4, 5]
y_data = [0, 2, 5, 8, 15, 27]
y2_data = [0, 1, 3, 5, 10, 20]

plt.axvline(3, color="orange", label="3-second mark")
plt.axhline(15, color="lightgrey", label="15-meter line")

plt.plot(x_data, y_data, color="r", marker="s", linestyle="", label="Fast car")
plt.plot(x_data, y2_data, color="seagreen", marker="o", linestyle=":", label="Slow car")

plt.xlabel("Time (s)")
plt.ylabel("Position (m)")

plt.xlim(0, 5)
plt.ylim(0, 30)

plt.legend()

plt.show()
