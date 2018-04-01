#include <bitset>
#include <cstdio>
#include <deque>
#include <vector>

#define MAX 10000

using namespace std;

void bfs(vector< vector< int > >& iGraph, bitset<(MAX + 1)>& bIsGoing, vector< pair< int, int > >& iAnswer) {

	vector< int > iDepth;
	int iMaxDepth = 0, iFrom, iI;
	deque< int > q;
	vector< int >::iterator it;

	iDepth.resize(iGraph.size());
	iDepth[0] = 0;

	q.push_back(0);

	while (q.empty() == false) {

		iFrom = q.front();
		q.pop_front();

		for (it = iGraph[iFrom].begin(); it != iGraph[iFrom].end(); it++) {

			q.push_back(*it);
			iDepth[*it] = iDepth[iFrom] + 1;

			if (iDepth[*it] > iMaxDepth)
				iMaxDepth = iDepth[*it];

		}

	}

	iAnswer.resize(iMaxDepth + 1);
	for (iI = 0; iI <= iMaxDepth; iI++)
		iAnswer[iI] = pair< int, int >(0, 0);

	for (iI = 0; iI < iGraph.size(); iI++) {
		iAnswer[iDepth[iI]].first++;
		if (bIsGoing[iI] == true)
			iAnswer[iDepth[iI]].second++;
	}

}

int main(void) {

	int iN, iM;
	int iI;
	int iParent;
	vector< vector< int > > iGraph;
	bitset<(MAX + 1)> bIsGoing;
	vector< pair< int, int > > iStats;

	scanf("%d %d", &iN, &iM);

	iGraph.resize(iN + 1);
	for (iI = 0; iI <= iN; iI++)
		iGraph[iI].clear();

	for (iI = 1; iI <= iN; iI++) {
		scanf("%d", &iParent);
		iGraph[iParent].push_back(iI);
	}

	bIsGoing.reset();
	for (iI = 0; iI < iM; iI++) {
		scanf("%d", &iParent);
		bIsGoing[iParent] = true;
	}

	bfs(iGraph, bIsGoing, iStats);

	for (iI = 1; iI < (iStats.size() - 1); iI++)
		printf("%.2lf ", ((double)iStats[iI].second / (double)iStats[iI].first) * 100);
	printf("%.2lf\n", ((double)iStats[iI].second / (double)iStats[iI].first) * 100);

	return 0;

}