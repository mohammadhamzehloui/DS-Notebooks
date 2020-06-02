#Function for calculating Z_score
def z_score(data):
        data=np.sort(rand)
        mean = np.mean(data)
        std= np.std(data)
        return [i for i in data if (i-mean)/std > 3]

#Creating a normal distribution.
mu, sigma = 0, 1
rand = np.random.normal(mu, sigma, 700)

#Creating 2 datasets, the original and the one with logs:

fig, axs = plt.subplots(ncols=2,figsize=(20,10))
with_log= sns.distplot(np.log(demo_agg.age),bins = 10, ax=axs[0])
with_log.set()
sns.distplot(demo_agg.age,bins = 10,ax=axs[1])
