#ifndef __UZH_Basic_H__
#define __UZH_Basic_H__

#include "core/include/SError.h"
#include "../include/ContainerBase.h"

namespace UZH {
  
  // pseudo-flexibility for different ntuples, also change in NtupleObjectNames.h
  typedef float floatingnumber;
  
  class Basic: public ContainerBase {
  
  public:
    
    // default c'tor with index of this Basic
    Basic( int idx = -1 );
    
    // default d'tor
    ~Basic();
    
    // flag as a good Basic
    void flagAsGood( bool good = true );
    
    // is a good Basic
    bool isGood() const;
    
    // get detail level
    int getLvl() const { return m_lvl; };
    
    int idx() const;
    int lvl() const;
    
    void checkLevel(int) const; //< deprecated
    void checkLevel(int, const char*) const;
    int  m_lvl;  
    
  private:
    bool  m_isGood;
    int m_idx;
    
  };
  
  inline void Basic::flagAsGood( bool good )   { m_isGood = good; }
  inline bool Basic::isGood() const            { return m_isGood; }
  inline int Basic::idx() const { return m_idx; }
  inline int Basic::lvl() const { return m_lvl; }
  
}

/// output operator for Basics
std::ostream& operator<<( std::ostream& out,
                          const UZH::Basic& rhs );

#endif //__UZH_Basic_H__
