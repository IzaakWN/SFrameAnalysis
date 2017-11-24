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

Particle::~Particle() { }

void Particle::calculateE() {
  // TODO: double check validity
  // TLorentzVector::SetXYZM https://root.cern.ch/doc/master/TLorentzVector_8h_source.html#l00342
  // TLorentzVector::SetXYZT https://root.cern.ch/doc/master/TLorentzVector_8h_source.html#l00335
  floatingnumber e = 0.0;
  if (*(m_m)>=0)
    e =     sqrt(pow(*(m_pt),2)*(1+pow(sinh(*(m_eta)),2)) + pow(*(m_m),2));
  else
    e = max(sqrt(pow(*(m_pt),2)*(1+pow(sinh(*(m_eta)),2)) - pow(*(m_m),2)),0.0);
  m_e = &(e); // set m_e
}

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
