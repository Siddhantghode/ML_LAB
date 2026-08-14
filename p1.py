import matplotlib.pyplot as plt
student=["x","y","Z"]
marks=[10,30,60]
plt.plot(student, marks,color="Red", marker="o", linewidth=3, markersize=4)
plt.title("Student Marks"  )
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
