#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

#include "olcConsoleGameEngine.h"

class PathfindingAstar : public olcConsoleGameEngine {
    public:
    OneLoneCoder_PathFinding()
	{
		m_sAppName = L"Path Finding";
	}
	struct Node {
		bool visited;
		Node* next, prev, top, botom;

	}
}