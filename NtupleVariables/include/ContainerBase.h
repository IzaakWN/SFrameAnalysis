#ifndef __UZH_CONTAINERBASE_H__
#define __UZH_CONTAINERBASE_H__

/**
 *  @short Extension for basic particle class to store additional variables
 *
 *         This class can be used to store additional variables in map.
 *         Some helper functions are available.
 *
 * @author Clemens Lange <Clemens.Lange@desy.de>
 *
 * $Rev: 39970 $
 * $Date: 2013-04-06 18:23:39 +0200 (Sat, 06 Apr 2013) $
 */

// STL include(s):
#include <map>
#include <vector>
#include <iostream>

// SFrame include(s):
#include "core/include/SError.h"


namespace UZH {

//   class printable {
//   
//   public:
//   
//     //this pure virtual method will be called to print the derived class' object.
//     virtual std::ostream& print(std::ostream& output) = 0;
//     virtual ~printable();
//   };


  class ContainerBase/*: public printable*/ {

  public:

    ContainerBase();
    virtual ~ContainerBase();

    virtual void Reset();

    //get and set functions
    void Set(std::string,int);
    void Set(std::string,double);

    inline void Set(std::string name, unsigned int val){
      Set(name, static_cast<int>(val));
    };

/*
    inline void Set(const char name, int val){
      Set(static_cast<std::string>(name), val);
    };

    inline void Set(const char name, unsigned int val){
      Set(static_cast<std::string>(name), static_cast<int>(val));
    };

	inline void Set(const char name, double val){
	  Set(static_cast<std::string>(name), val);
	};
*/

	int GetInt(std::string) const;
	double GetDouble(std::string) const;
	std::vector<std::string> GetIntKeys();
	std::vector<std::string> GetDoubleKeys();

     //Print the list content
     std::ostream& print(std::ostream& out);

  private:

    std::map<std::string,int> map_int;
    std::map<std::string,double> map_double;

  }; // class ContainerBase

}; // namespace UZH


  /// output operator for ContainerBase
  //std::ostream& operator<<( std::ostream& out, UZH::ContainerBase& rhs );


#endif // __UZH_CONTAINERBASE_H__
