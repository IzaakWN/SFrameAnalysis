#include "../include/Particle.h"
//#include "TMath.h"
#include <cmath>

using namespace std;
using namespace UZH;

Particle::Particle() :
  m_e( 0 ),
  m_pt( 0 ),
  m_eta( 0 ),
  m_phi( 0 ),
  m_m( 0 )
{ }

Particle::~Particle()
{ }

floatingnumber Particle::DeltaR(const Particle* p) const {
  Double_t deta = *(m_eta) - p->eta();
  Double_t dphi = *(m_phi) - p->phi();
  double pi = TMath::Pi();
  double twopi = 2*pi;
  while (dphi >= pi) dphi -= twopi;
  while (dphi < -pi) dphi += twopi;
  return sqrt( deta*deta+dphi*dphi );
}


floatingnumber Particle::DeltaR(const Particle p) const {
  Double_t deta = *(m_eta) - p.eta();
  Double_t dphi = *(m_phi) - p.phi();
  double pi = TMath::Pi();
  double twopi = 2*pi;
  while (dphi >= pi) dphi -= twopi;
  while (dphi < -pi) dphi += twopi;
  return sqrt( deta*deta+dphi*dphi );
}


ostream& operator<<( ostream& out,
                     const Particle& rhs ) {

  out << " m:"   << rhs.m()
      << " e:"   << rhs.e()
      << " pt:"  << rhs.pt()
      << " eta:" << rhs.eta()
      << " phi:" << rhs.phi();

  return out;
}

bool sortParticlePt::operator()( const Particle& p1, 
                                 const Particle& p2 ) {
  return ( p1.pt() > p2.pt() ) ? true : false;
}

TLorentzVector* Particle::getTLV() const {
  
  TLorentzVector* tlv = new TLorentzVector();
  tlv->SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;
  
}
