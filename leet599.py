class Solution(object):
    def findRestaurant(self, list1, list2):
        anshash = {}
        uphash = {}
        downhash = {}
        l1 = len(list1)
        l2 = len(list2)
        mxlen = l1 if l1 > l2 else l2
        mnidx = 2000


        for i in range(mxlen):
            if i < l1: # make the uphash
                uphash.setdefault(list1[i], i)
                if downhash.get(list1[i], None) != None:
                    if i + downhash[list1[i]] <= mnidx:
                        mnidx = i + downhash[list1[i]]
                        anshash[list1[i]] = mnidx

            if i < l2: # make the downhash
                downhash.setdefault(list2[i], i)
                if uphash.get(list2[i], None) != None:
                    if i + uphash[list2[i]] <= mnidx:
                        mnidx = i + uphash[list2[i]]
                        anshash[list2[i]] = mnidx
        return list(anshash.keys())

l1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]

l3 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
l4 = ["KFC", "Shogun", "Burger King"]

l5 = ["Shogun","Tapioca Express","Burger King","KFC"]
l6 = ["KFC","Burger King","Tapioca Express","Shogun"]

print(Solution().findRestaurant(l5, l6))