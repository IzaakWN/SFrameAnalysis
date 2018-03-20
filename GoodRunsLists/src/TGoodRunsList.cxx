// $Id: TGoodRunsList.cxx 45093 2010-08-20 11:58:27Z krasznaa $

// SFrame include(s):
#include "core/include/SLogger.h"

// Local include(s):
#include "../include/TGoodRunsList.h"

ClassImp( Root::TGoodRunsList );

namespace Root {

   TGoodRunsList::TGoodRunsList()
      : std::map< Int_t, TGoodRun >(), TNamed( "noname","notitle" ),
        m_checkGRLInfo( kFALSE ), m_hasRun( kFALSE ), m_hasLB( kFALSE ),
        m_prevRun( -10 ), m_prevLB( -10 ) {

   }

   TGoodRunsList::TGoodRunsList( const char* name )
      : std::map< Int_t, TGoodRun >(), TNamed( name, "notitle" ),
        m_checkGRLInfo( kFALSE ), m_hasRun( kFALSE ), m_hasLB( kFALSE ),
        m_prevRun( -10 ), m_prevLB( -10 ) {

   }

   TGoodRunsList::TGoodRunsList( const Root::TGoodRunsList& other )
      : std::map< Int_t, TGoodRun >( other ), TNamed( other ),
        m_version( other.m_version ), m_metadata( other.m_metadata ),
        m_checkGRLInfo( other.m_checkGRLInfo ), m_hasRun( other.m_hasRun ),
        m_hasLB( other.m_hasLB ), m_prevRun( other.m_prevRun ),
        m_prevLB( other.m_prevLB ) {

   }
   
   TGoodRunsList& TGoodRunsList::operator=( const TGoodRunsList& other ) {
      
      if( &other == this ) {
         return *this;
      }
      
      std::map< Int_t, TGoodRun >::operator=( other );
      TNamed::operator=( other );
      m_version = other.m_version;
      m_metadata = other.m_metadata;
      m_checkGRLInfo = other.m_checkGRLInfo;
      m_hasRun = other.m_hasRun;
      m_hasLB = other.m_hasLB;
      m_prevRun = other.m_prevRun;
      m_prevLB = other.m_prevLB;
      
      return *this ;
   }

   void TGoodRunsList::AddGRL( const TGoodRunsList& other ) {

      // ensure version and metadata are identical
      Bool_t same = this->HasSameGRLInfo( other );
      if( m_checkGRLInfo || other.GetCheckGRLInfo() ) {
         if( ! same ) {
            SLogger logger( "TGoodRunsList" );
            logger << WARNING << "Incompatible NamedLumiRanges: " << SLogger::endmsg;
            this->Summary( kFALSE );
            other.Summary( kFALSE );
            logger << WARNING << "Not adding GoodRunsList." << SLogger::endmsg;
            return;
         }
      }
      
      const TGoodRunsList& diffgrl = this->GetPartOnlyIn( other );
      
      std::map< Int_t, TGoodRun >::const_iterator itr;
      // Store diffgrl goodrunslist
      for( itr = diffgrl.begin(); itr != diffgrl.end(); ++itr ) {
         if( this->find( itr->first ) != this->end() ) { // overlapping runnumbers
            TGoodRun grun = itr->second.GetSumWith( this->find( itr->first )->second );
            if( ! grun.IsEmpty() ) ( *this )[ itr->first ] = grun;
         } else if( ! itr->second.IsEmpty() ) { // store rest directly
            ( *this )[ itr->first ] = itr->second;
         }
      }

      return;
   }

   const TGoodRunsList TGoodRunsList::GetOverlapWith( const TGoodRunsList& other ) const {

      TGoodRunsList overlapgrl;
      overlapgrl.SetName( "Overlap of GRLs" );

      // ensure version and metadata are identical
      Bool_t same = this->HasSameGRLInfo( other );
      if( m_checkGRLInfo || other.GetCheckGRLInfo() ) { 
         if( ! same ) {
            SLogger logger( "TGoodRunsList" );
            logger << WARNING << "Incompatible NamedLumiRanges: " << SLogger::endmsg;
            this->Summary( kFALSE );
            other.Summary( kFALSE );
            logger << WARNING << "Returning empty GoodRunsList." << SLogger::endmsg;
            return overlapgrl;
         }
      }
      if( same ) {
         overlapgrl.SetName( this->GetName() );
         overlapgrl.SetVersion( this->GetVersion() );
         overlapgrl.SetMetaData( this->GetMetaData() );
      }

      // Store goodruns
      std::map< Int_t, TGoodRun >::const_iterator itr = this->begin();
      for( ; itr != this->end(); ++itr ) {
         if( other.find( itr->first ) != other.end() ) { // check runnumbers
            TGoodRun grun = itr->second.GetOverlapWith( other.find( itr->first )->second ) ;
            if( ! grun.IsEmpty() ) {
               grun.Sort(); // sort lumiblock ranges before storage
               overlapgrl[ itr->first ] = grun;
            }
         }
      }

      return overlapgrl;
   }

   const TGoodRunsList TGoodRunsList::GetSumWith( const TGoodRunsList& other ) const {

      TGoodRunsList sumgrl;
      sumgrl.SetName( "Sum of GRLs" );

      // ensure version and metadata are identical
      Bool_t same = this->HasSameGRLInfo( other );
      if( m_checkGRLInfo || other.GetCheckGRLInfo() ) {
         if( ! same ) { 
            SLogger logger( "TGoodRunsList" );
            logger << WARNING << "Incompatible NamedLumiRanges: " << SLogger::endmsg;
            this->Summary( kFALSE );
            other.Summary( kFALSE );
            logger << WARNING << "Returning empty GoodRunsList." << SLogger::endmsg;
            return sumgrl;
         }
      }
      if ( same ) {
         sumgrl.SetName( this->GetName() );
         sumgrl.SetVersion( this->GetVersion() );
         sumgrl.SetMetaData( this->GetMetaData() );
      }

      std::map< Int_t, TGoodRun >::const_iterator itr;
      // Store this goodruns
      for( itr = this->begin(); itr != this->end(); ++itr ) {
         if( other.find( itr->first ) != other.end() ) { // check runnumbers
            TGoodRun grun = itr->second.GetSumWith( other.find( itr->first )->second ) ;
            if( ! grun.IsEmpty() ) sumgrl[ itr->first ] = grun;
         } else if( ! itr->second.IsEmpty() ) { // store difference
            sumgrl[ itr->first ] = itr->second;
         }
      }
      // Store remaining other goodruns
      for( itr = other.begin(); itr != other.end(); ++itr ) {
         if( sumgrl.find( itr->first ) == sumgrl.end() &&
             ! itr->second.IsEmpty() ) { // check for remaining runnumbers
            sumgrl[ itr->first ] = itr->second;
         }
      }

      return sumgrl;
   }

   const TGoodRunsList TGoodRunsList::GetPartOnlyIn( const TGoodRunsList& other ) const {

      return other.GetPartNotIn( *this );
   }

   const TGoodRunsList TGoodRunsList::GetPartNotIn( const TGoodRunsList& other ) const {

      TGoodRunsList notinother;
      notinother.SetName( "Difference of GRLs" );  

      // ensure version and metadata are identical
      Bool_t same = this->HasSameGRLInfo( other );
      if( m_checkGRLInfo || other.GetCheckGRLInfo() ) { 
         if( ! same ) {
            SLogger logger( "TGoodRunsList" );
            logger << WARNING << "Incompatible NamedLumiRanges: " << SLogger::endmsg;
            this->Summary( kFALSE );
            other.Summary( kFALSE );
            logger << WARNING << "Returning empty GoodRunsList." << SLogger::endmsg;
            return notinother;
         }
      }
      if( same ) {
         notinother.SetName( this->GetName() );
         notinother.SetVersion( this->GetVersion() );
         notinother.SetMetaData( this->GetMetaData() );
      }

      std::map< Int_t, TGoodRun >::const_iterator itr;
      // How to store this goodrun ?
      for( itr = this->begin(); itr != this->end(); ++itr ) {
         if( other.find( itr->first ) != other.end() ) { // check runnumbers
            TGoodRun notinrun = itr->second.GetPartNotIn( other.find( itr->first )->second );
            if( ! notinrun.IsEmpty() ) notinother[ itr->first ] = notinrun;
         } else if( ! itr->second.IsEmpty() ) { // store difference
            notinother[ itr->first ] = itr->second;
         }
      }

      return notinother;
   }

   Bool_t TGoodRunsList::HasRun( const Int_t& runnr ) const {

      // run searched same as previous run?
      if( runnr == m_prevRun ) { return m_hasRun; }

      m_prevRun = runnr;
      m_hasRun = ( this->find( runnr ) != this->end() );
      return m_hasRun;
   }

   Bool_t TGoodRunsList::HasRunLumiBlock( const Int_t& runnr,
                                          const Int_t& lumiblocknr ) const {

      Bool_t pass = kFALSE;

      if( this->HasRun( runnr ) ) {
         // LB searched same as previous LB?
         if( lumiblocknr == m_prevLB ) { return m_hasLB; }
         m_prevLB = lumiblocknr;
         m_hasLB  = ( this->find( runnr ) )->second.HasLB( lumiblocknr );
         pass = m_hasLB;
      }

      return pass;
   }

   Bool_t TGoodRunsList::HasTriggerInfo() const {

      std::map< TString, TString >::const_iterator itr = m_metadata.begin(); 
      for( ; itr != m_metadata.end(); ++itr ) {
         TString triggername = itr->first;
         triggername.ToLower();
         if( triggername.BeginsWith( "trigger" ) &&
             itr->second.Length() > 0 ) return kTRUE;
      }

      return kFALSE;
   }

   Bool_t TGoodRunsList::HasOverlapWith( const TGoodRunsList& other, bool verb ) const {

      const TGoodRunsList overlapgrl = this->GetOverlapWith( other );
      bool isEmpty = overlapgrl.IsEmpty();
      if( ! isEmpty && verb) overlapgrl.Summary( true );

      return ! isEmpty; 
   }

   void TGoodRunsList::Summary( Bool_t verbose ) const {

      // TNamed print
      Print();

      SLogger logger( "TGoodRunsList" );
      // Versioning and metadata info
      logger << INFO << "Version: " << m_version << SLogger::endmsg;
      std::map< TString, TString >::const_iterator titr = m_metadata.begin();
      for( ; titr != m_metadata.end(); ++titr ) {
         logger << INFO << "Metadata: " << titr->first << " : "
                << titr->second << SLogger::endmsg;
      }

      logger << INFO << "Number of runs: " << this->size() << SLogger::endmsg;

      // Info about runs
      if( verbose ) {
         std::map<Int_t,Root::TGoodRun>::const_iterator itr = this->begin();
         std::map<Int_t,Root::TGoodRun>::const_iterator end = this->end();
         for( ; itr != end; ++itr ) itr->second.Summary();
      }

      return;
   }

   const std::vector< int > TGoodRunsList::GetRunlist() const {

      std::vector< int > runlist;

      std::map< Int_t, TGoodRun >::const_iterator itr = this->begin();
      std::map< Int_t, TGoodRun >::const_iterator end = this->end();
      for( ; itr != end; ++itr ) runlist.push_back( itr->first );

      return runlist;
   }

   const std::vector< TGoodRun > TGoodRunsList::GetGoodRuns() const {

      std::vector< TGoodRun > runlist;

      std::map< Int_t, TGoodRun >::const_iterator itr = this->begin();
      std::map< Int_t, TGoodRun >::const_iterator end = this->end();
      for( ; itr != end; ++itr ) runlist.push_back( itr->second );

      return runlist;
   }

   const std::vector< std::string > TGoodRunsList::GetTriggerList() const {

      std::vector< std::string > triggerchains;

      std::map< TString, TString >::const_iterator itr = m_metadata.begin();
      for( ; itr != m_metadata.end(); ++itr ) {
         TString triggername = itr->first;
         triggername.ToLower();
         if( triggername.BeginsWith( "trigger" ) &&
             itr->second.Length() > 0 ) triggerchains.push_back( itr->second.Data() );
      }

      return triggerchains;
   }

   const std::vector< std::string > TGoodRunsList::GetStreamList() const {

      std::vector< std::string > streamlist;

      std::map< TString, TString >::const_iterator itr = m_metadata.begin();
      for( ; itr != m_metadata.end(); ++itr ) {
         TString streamname = itr->first;
         streamname.ToLower(); 
         if( streamname.BeginsWith( "stream" ) &&
             itr->second.Length() > 0 ) streamlist.push_back( itr->second.Data() );
      }

      return streamlist;
   }

   Bool_t TGoodRunsList::HasSameGRLInfo( const TGoodRunsList& other ) const {

      SLogger logger( "TGoodRunsList" );
      Bool_t same( kTRUE );

      /// check names
      same = same && ( TString( this->GetName() ) == TString( other.GetName() ) );
      if( ! same ) {
         logger << DEBUG << "Incompatible names: <" << this->GetName() << "> <"
                << other.GetName() << ">" << SLogger::endmsg;
         return kFALSE;
      }
      /// check versions
      same = same && ( this->GetVersion() == other.GetVersion() );
      if( ! same ) { 
         logger << DEBUG << "Incompatible versions: <" << this->GetVersion() << "> <"
                << other.GetVersion() << ">" << SLogger::endmsg;
         return kFALSE;
      }
      /// check metadata size
      same = same && ( this->GetMetaData().size() == other.GetMetaData().size() );
      if( ! same ) {
         logger << DEBUG << "Incompatible metadata sizes: <" << this->GetMetaData().size()
                << "> <" << other.GetMetaData().size() << ">" << SLogger::endmsg;
         return kFALSE;
      }
      /// check metadata elements
      std::map< TString, TString >::const_iterator mitr = this->GetMetaData().begin();
      for( ; mitr != this->GetMetaData().end() && same; ++mitr ) {
         if( other.GetMetaData().find( mitr->first ) != other.GetMetaData().end() ) {
            same = same && ( mitr->second ==
                             ( other.GetMetaData().find( mitr->first ) )->second );
            if( ! same ) { logger << DEBUG << "Incompatible metadata: " << mitr->first 
                                  << " : <" << mitr->second << "> <"
                                  << ( other.GetMetaData().find( mitr->first ) )->second
                                  << ">" << SLogger::endmsg;
            }
         } else same = kFALSE; 
      }

      return same;
   }

   Bool_t TGoodRunsList::IsEmpty() const {

      if( this->empty() ) return kTRUE;

      Bool_t isEmpty( kTRUE );
      std::map< Int_t, TGoodRun >::const_iterator litr = this->begin();
      for( ; litr != this->end() && isEmpty; ++litr )
         isEmpty = isEmpty && litr->second.IsEmpty();

      return isEmpty;
   }

   const TString TGoodRunsList::GetSuggestedName() const {

      if( this->IsEmpty() ) return "grl_empty";

      Int_t beginrun( -1 ), endrun( -1 ), beginlb( -1 ), endlb( -1 );

      TGoodRun begingr = this->begin()->second;
      TGoodRun endgr   = this->rbegin()->second;

      if( ! begingr.IsEmpty() ) {
         beginrun = begingr.GetRunNumber();
         beginlb = begingr.begin()->Begin();
      }
      if( ! endgr.IsEmpty() ) {
         endrun = endgr.GetRunNumber();
         endlb = endgr.rbegin()->End(); 
      }

      return Form( "grl_%d.%d-%d.%d", beginrun, beginlb, endrun, endlb );
   }

   void TGoodRunsList::AddRunLumiBlock( const Int_t& runnr, const Int_t& lumiblocknr ) {

      if( runnr < 0 || lumiblocknr < 0 ) return;
      if( this->HasRunLumiBlock( runnr, lumiblocknr ) ) return;

      std::map< Int_t, TGoodRun >::iterator itr = this->find(runnr);
      if( itr == this->end() ) {
         this->insert( std::pair< Int_t, TGoodRun >( runnr, TGoodRun( runnr ) ) );
         itr = this->find( runnr );
      }

      itr->second.AddLB( lumiblocknr );

      return;
   }

   void TGoodRunsList::Compress() {

      std::map< Int_t, TGoodRun >::iterator itr = this->begin();
      for( ; itr != this->end(); ++itr )
         itr->second.Compress();

      return;
   }

} // namespace Root
