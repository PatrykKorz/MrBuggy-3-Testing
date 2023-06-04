import matplotlib.pyplot as plt

# histogram
defects = {
    'Blocker': 0,
    'Critical': 4,
    'Major': 2,
    'Minor': 3
}

defect_types = list(defects.keys())
defect_counts = list(defects.values())

plt.bar(defect_types, defect_counts)
plt.xlabel('Defect type')
plt.ylabel('Number of defects')
plt.title('Histogram of defects')
plt.yticks([0, 1 ,2,3, 4])
plt.show()


# diagram
passed_tests = 93
failed_tests = 15

labels = ['Passed tests', 'Failed tests']
sizes = [passed_tests, failed_tests]
colors = ['#1f77b4', '#ff7f0e']

plt.pie(sizes, labels=labels, colors=colors, autopct=lambda x: f'{x:.0f}% ({x*sum(sizes)/100:.0f})')
plt.axis('equal')
plt.title('Test results')

plt.show()
