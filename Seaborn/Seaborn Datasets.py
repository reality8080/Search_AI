import seaborn as sns
print(sns.get_dataset_names())
# Một số tập dữ liệu có sẵn của seaborn
# ['anagrams', 'anscombe', 'attention', 
#  'brain_networks', 'car_crashes', 'diamonds', 
#  'dots', 'dowjones', 'exercise', 'flights',
#  'fmri', 'geyser', 'glue', 'healthexp', 
#  'iris', 'mpg', 'penguins', 'planets', 
#  'seaice', 'taxis', 'tips', 'titanic']
# Một số tập dữ liệu quan trọng
tips=sns.load_dataset("tips")
iris=sns.load_dataset("iris")
titanic=sns.load_dataset("titanic")
planets=sns.load_dataset("planets")
print(tips.head(),iris.head(),titanic.head(),planets.head(), sep="\n")