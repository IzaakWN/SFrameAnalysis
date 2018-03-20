// $Id: TGoodRunsListReader.cxx 45093 2010-08-20 11:58:27Z krasznaa $

#include "../include/TGoodRunsListReader.h"

using namespace std;

namespace Root {

   TGoodRunsListReader::TGoodRunsListReader( Bool_t checkGRLInfo )
      : TObject(), m_logger( "TGoodRunsListReader" ) {

      m_grlvec.SetCheckGRLInfo( checkGRLInfo );
   }

   TGoodRunsListReader::TGoodRunsListReader( const TString& dataCardName, Bool_t checkGRLInfo )
      : TObject(), m_logger( "TGoodRunsListReader" ) {
      
      //m_logger << INFO << "TGoodRunsListReader:1 " << dataCardName << SLogger::endmsg;
      m_dataCardList.push_back( dataCardName );
      m_grlvec.SetCheckGRLInfo( checkGRLInfo );
   }

   void TGoodRunsListReader::Reset() {

      m_grlvec.Reset();
      m_dataCardList.clear();
      m_xmlstringList.clear();
      m_xmlstring=""; //Clear() only works in root5.24
      m_dataCardName="";

      return;
   }

   Bool_t TGoodRunsListReader::Interpret() {
      
      Bool_t jsonInterpret( kTRUE );

      if( m_dataCardList.empty() && m_xmlstringList.empty() ) {
         m_logger << WARNING << "No xml data-card or string set. Return false."
                  << SLogger::endmsg;
         return kFALSE;
      }

      Bool_t parseCode( true );
      // parse JSON here instead of XML
      // TDOMParser* xmlparser = new TDOMParser();
      Json::Reader jsonReader;
      Json::Value jsonRoot;

      //////////////////////////////////////////////////////////////////////
      
      // --------------- xml file read
      for( unsigned int j = 0; j < m_dataCardList.size() && jsonInterpret; ++j ) {
         m_dataCardName = m_dataCardList[ j ];
         //m_logger << INFO << "Interpret: " << dataCardName << SLogger::endmsg;
         
         if( ! m_dataCardName.IsNull() ) {
            m_logger << DEBUG << "Read xml data-card: \"" << m_dataCardName
                     << "\"" << SLogger::endmsg;
            std::ifstream ifile(m_dataCardName);
            parseCode = jsonReader.parse(ifile, jsonRoot);
         } else {
            m_logger << WARNING << "No xml data-card set. Skip." << SLogger::endmsg;
            continue;
         }

         m_logger << DEBUG << "XML parser returned code: " << parseCode << SLogger::endmsg;
         if( !parseCode ) { 
            m_logger << ERROR << "loading of xml document failed" << SLogger::endmsg;
            jsonInterpret = kFALSE;
         } else {
            // --------------- parse JobConfiguration
            m_logger << INFO << "JSON file contains " << jsonRoot.size() << " runs." << SLogger::endmsg;
            TGoodRunsList grl( m_dataCardName.Data() );
            for( Json::ValueIterator itr = jsonRoot.begin() ; itr != jsonRoot.end() ; ++itr ) {
              // TGoodRun needs a run number and lumi blocks
              TGoodRun goodrun;
              goodrun.SetRunNumber( stoi(itr.key().asString()) );
              m_logger << DEBUG << "Run (key): " << itr.key() << SLogger::endmsg;
              Json::Value dataNode = *itr;
              m_logger << DEBUG << dataNode.type() << " - size: " << dataNode.size() << SLogger::endmsg;
              for (unsigned int i=0; i<dataNode.size(); ++i) { // loop over lumi block for a single run
                TLumiBlockRange lbr;
                bool startBlock = true;
                m_logger << DEBUG << "Block: " << dataNode[i] << SLogger::endmsg;
                for( Json::ValueConstIterator itr = dataNode[i].begin() ; itr != dataNode[i].end() ; ++itr ) {
                  m_logger << DEBUG << "Block (itr): " << *itr << " - type: " << (*itr).type() << SLogger::endmsg;
                  if (startBlock) {
                    m_logger << DEBUG << "Begin Lumi Block: " << *itr << SLogger::endmsg;
                    lbr.SetBegin( (*itr).asInt() );
                    // lbr.SetEnd( 2147483647 ); // set in case lb turns out to be open-ended
                    startBlock = false;
                  }
                  else {
                    m_logger << DEBUG << "End Lumi Block: " << *itr << SLogger::endmsg;
                    lbr.SetEnd( (*itr).asInt() );
                    startBlock = true;
                  }
                } // end loop over single lumi block
                if( ! lbr.IsEmpty() ) {goodrun.push_back( lbr );
                  m_logger << DEBUG << "push back LBR!" << SLogger::endmsg;
                }
                else m_logger << WARNING << "LBR empty!" << SLogger::endmsg;
              } // end loop over lumi block for a single run
              if( ! goodrun.IsEmpty() ) { grl[ goodrun.GetRunNumber() ] = goodrun ; 
                m_logger << DEBUG << "Adding Run: " << goodrun.GetRunNumber() << SLogger::endmsg;
              }
              else m_logger << WARNING << "Run empty!" << SLogger::endmsg;
            } // end loop over runs
            if( ! grl.IsEmpty() ) m_grlvec.push_back( grl );
            else m_logger << WARNING << "GRL empty!" << SLogger::endmsg;
         } // end parse JSON file
      }
      m_dataCardList.clear(); // Can now add fresh xml files

      return jsonInterpret;
   }


   const TGoodRunsList
   TGoodRunsListReader::GetMergedGoodRunsList( const BoolOperation& operation ) const {

      return m_grlvec.GetMergedGoodRunsList( operation ); 
   }

   const TGoodRunsList
   TGoodRunsListReader::GetGoodRunsList( unsigned int idx ) const {

      return m_grlvec.GetGoodRunsList( idx );
   }

   const TGRLCollection
   TGoodRunsListReader::GetMergedGRLCollection( const BoolOperation& operation ) const {

      return m_grlvec.GetMergedGRLCollection( operation );
   }

} // namespace Root
