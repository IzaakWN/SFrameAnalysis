// Dear emacs, this is -*- c++ -*-
// $Id: NtupleObjectNames.h 42092 2014-03-19 15:37:47Z lrehnisc $

#ifndef SFRAME_NtupleVARIABLES_NtupleObjectNames_H
#define SFRAME_NtupleVARIABLES_NtupleObjectNames_H

// STL include(s):
#include <map>
#include <iostream>

// ROOT include(s):
#include <TString.h>

// SFrame include(s):
#include "core/include/SError.h"

namespace Ntuple {

  /**
   *  @short Class that returns the right branch names for ntuple type
   *
   *         This class can be used to return the right branch names 
   *         ntuple type, for instance for ntuples created by the SingleTopDPDMaker
   *         code or SM Ntuples.
   *
   * @author Clemens Lange <Clemens.Lange@desy.de>
   *
   * $Rev: 42092 $
   * $Date: 2014-03-19 16:37:47 +0100 (Wed, 19 Mar 2014) $
   */
  // pseudo-flexibility for different ntuples, also change in Particle.h
  typedef float floatingnumber;
  class NtupleObjectNames {

    public:
      /// Constructor
      NtupleObjectNames( const TString& ntupleType = "UZHCMSNtuple" );
      
      /// Return names saved in map 
      TString getName( const TString& name );
      TString getPrefix( const TString& name );


    private:
    
      /// Fill the map according to ntupleType
      void FillMap ( TString ntupleType ) throw( SError );
      
      /// functions filling the name maps
      void FillUZHCMSNtuple();

      //
      // THE name map
      //
      std::map<TString, TString> m_names;
      
      // and THE prefix map
      std::map<TString, TString> m_prefixes;

  }; // class NtupleObjectNames
  
} // namespace Ntuple

#endif // SFRAME_NtupleVARIABLES_NtupleObjectNames_H
