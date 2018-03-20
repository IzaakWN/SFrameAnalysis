// Dear emacs, this is -*- c++ -*-
// $Id: TGoodRunsListReader.h 45093 2010-08-20 11:58:27Z krasznaa $
#ifndef SFRAME_GOODRUNSLISTS_TGoodRunsListReader_H
#define SFRAME_GOODRUNSLISTS_TGoodRunsListReader_H

// System include(s):
#include <cstdlib>
#include <fstream>
#include <wordexp.h>
//#include <regex>

// STL include(s):
#include <vector>
#include <string>

// ROOT include(s):
#include "TObject.h"
#include "TString.h"
#include "TDOMParser.h"
#include "TXMLNode.h"
#include "TXMLDocument.h"
#include "TXMLAttr.h"
#include "TList.h"

// JSON include(s):
#include "../include/json.h"

// SFrame include(s):
#include "core/include/SLogger.h"

// Local include(s):
#include "TGRLCollection.h"
#include "TGoodRun.h"
#include "TGoodRunsList.h"
#include "../include/TLumiBlockRange.h"
#include "../include/StrUtil.h"




// Forward declaration(s):
class TXMLNode;

namespace Root {

   /**
    *  @short Class capable of reading GRL XMLs
    *
    *         This class should be used to interpret GRL XML files in an analysis, and turn
    *         them into TGoodRunsList objects.
    *
    * @author Max Baak <mbaak@cern.ch> - CERN, Switzerland
    * @author Attila Krasznahorkay <Attila.Krasznahorkay@cern.ch>
    *
    * $Revision: 45093 $
    * $Date: 2010-08-20 13:58:27 +0200 (Fri, 20 Aug 2010) $
    */
   class TGoodRunsListReader : public TObject {

   public:
      /// Default constructor specifying if GRL info should be checked
      TGoodRunsListReader( Bool_t checkGRLInfo = kFALSE );
      /// Constructor specifying one input XML file
      TGoodRunsListReader( const TString& dataCardName, Bool_t checkGRLInfo = kFALSE );

      /// Function reading in the specified XML(s)
      Bool_t Interpret();     

      /// Get the XML string that was last interpreted
      inline const TString& GetXMLString()   const { return m_xmlstring; }
      /// Get the XML file name that was last interpreted
      inline const TString& GetXMLFilename() const { return m_dataCardName; }

      /// Add a file to the list of files to interpret
      inline void AddXMLFile( const TString& xmlfile ) { m_dataCardList.push_back( xmlfile ); }
      /// Add a string to the list of strings to interpret
      inline void AddXMLString( const TString& xmlstring ) {
         m_xmlstringList.push_back( xmlstring );
      }
      /// Set this one string to be interpreted
      inline void SetXMLString( const TString& xmlstring ) {
         Reset();
         m_xmlstringList.push_back( xmlstring );
      }
      /// Set this one file to be interpreted
      inline void SetXMLFile( const TString& xmlfile ) {
         Reset();
         m_dataCardList.push_back( xmlfile );
      }
      /// Set whether or not to check the GRL info in various operations
      inline void SetCheckGRLInfo( Bool_t check = kTRUE ) { m_grlvec.SetCheckGRLInfo( check ); }

      /// Get a merged version of the GRLs
      const TGoodRunsList
      GetMergedGoodRunsList( const Root::BoolOperation& operation = OR ) const;
      /// Get the GRL at a certain index
      const TGoodRunsList  GetGoodRunsList( unsigned int idx ) const;
      /// Get the full GRL collection
      inline const TGRLCollection GetGRLCollection() const { return m_grlvec; }
      /// Get a merged version of the GRL collection
      const TGRLCollection
      GetMergedGRLCollection( const Root::BoolOperation& operation = OR ) const;

      /// Reset the object to default values
      void Reset();

   private:

      TString m_xmlstring; ///< XML string that was interpreted last
      TString m_dataCardName; ///< XML file that was interpreted last
      std::vector< TString > m_dataCardList; ///< XML files to interpret
      std::vector< TString > m_xmlstringList; ///< XML strings to interpret

      TGRLCollection m_grlvec; ///< Object holding the information read from XML

      mutable SLogger m_logger; ///< Private logger object

   }; // class TGoodRunsListReader

} // namespace Root

#endif // SFRAME_GOODRUNSLISTS_TGoodRunsListReader_H
