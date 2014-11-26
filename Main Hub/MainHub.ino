int node = 5;
int looper = 0;
int graph[5][5] = { {0,2,0,4,0},
                    {0,0,2,0,0},
                    {4,0,0,2,0},
                    {0,4,0,0,2},
                    {2,0,4,0,0} };

void setup(){
  Serial.begin(9600);

  //cannot write and read file
  /*FILE *f;
  f = fopen("graph.txt", "w");
  if (f == NULL){
    initiateGraph();
  }*/
}

void loop(){
  int iSour = -1;
  int iDest = -1;

  Serial.print("\n");
  while(iSour == -1){
    iSour = Serial.read();
    if(iSour != -1){
      break;
    }
  }

  while(iDest == -1){
    iDest = Serial.read();
    if(iDest != -1){
      break;
    }
  }
  
  iSour = asciiToStation(iSour);
  iDest = asciiToStation(iDest);

  generatePath(iSour, iDest, graph);
}

void printGraph(int graph[5][5]){
  for(int outter = 0; outter<node; outter++){
    for(int inner = 0; inner<node; inner++){
      //Serial.print("graph[%d][%d] = %d\n", outter, inner, graph[outter][inner]);
      Serial.print(graph[outter][inner]);
      Serial.print(",");
    }
    Serial.print("\n");
  }
}

//Generate a path from source to destination
void generatePath(int iSource, int iDestination, int graph[5][5]){
  int currNode;
  int i = 1;
  int possible[5] = {0,0,0,0,0};
  //currNode starts at source
  currNode = iSource;

  //Parse through matrix and found possible routes
  //extract total, weight, station, weight, station
  for(int counter = 0; counter<5; counter++){
    if(graph[currNode-1][counter] != 0){
      possible[0] = possible[0]+1;
      possible[i] = graph[currNode-1][counter];
      i++;
      possible[i] = counter+1;
      i++;
    }
  }
  if(possible[0] == 1){
    currNode = possible[2];
  }
  else{
    currNode = possible[2];
  }
  Serial.print(currNode);
  if(currNode==iDestination){
    Serial.print("Done");
  }
  else{
    generatePath(currNode, iDestination, graph);
  }
}

//Converts Read value(in ascii) and turn a station number
int asciiToStation(int iStation){
  switch(iStation){
    case 49:
      iStation = 1;
      break;
    case 50:
      iStation = 2;
      break;
    case 51:
      iStation = 3;
      break;
    case 52:
      iStation = 4;
      break;
    case 53:
      iStation = 5;
      break;
  }
  return iStation;
}