#include "../include/Basic.h"
//#include "TMath.h"
#include <cmath>

using namespace std;
using namespace UZH;

Basic::Basic( int idx ) :
  ContainerBase(),
  m_isGood( false ),
  m_idx( idx )
{ }

Basic::~Basic()
{ }

void Basic::checkLevel(int detailLvl) const {
  if (m_lvl < detailLvl) {
     throw SError( "Property not available. Change Detail Level!", SError::StopExecution );
  }
}
        
void Basic::checkLevel(int detailLvl, const char*property) const {
  if (m_lvl < detailLvl) {
    string msg = "Property ";
    msg += property;
    msg += " not available. Change Detail Level!";
     throw SError( msg.c_str(), SError::StopExecution );
  }
}
        
ostream& operator<<( ostream& out, const Basic& rhs ) {

  out << " idx:" << rhs.idx()
      //<< " lvl:" << rhs.lvl()
      ;

  return out;
}

