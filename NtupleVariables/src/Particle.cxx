#include "../include/Particle.h"
//#include "TMath.h"
#include <cmath>

using namespace std;
using namespace UZH;

Particle::Particle() :
  m_e(   0 ),
  m_pt(  0 ),
  m_eta( 0 ),
  m_phi( 0 ),
  m_m(   0 )
{ }

Particle::~Particle() { }

floatingnumber Particle::calculateE() {
  // TODO: double check validity
  // TLorentzVector::SetXYZM https://root.cern.ch/doc/master/TLorentzVector_8h_source.html#l00342
  // TLorentzVector::SetXYZT https://root.cern.ch/doc/master/TLorentzVector_8h_source.html#l00335
  floatingnumber e_ = 0.0;
  if (*(m_m)>=0)
    e_ = sqrt(     pow(*(m_pt),2)*(1+pow(sinh(*(m_eta)),2)) + pow(*(m_m),2)      );
  else
    e_ = sqrt(max( pow(*(m_pt),2)*(1+pow(sinh(*(m_eta)),2)) - pow(*(m_m),2), 0.0 ));
  
  return e_;
}

floatingnumber Particle::DeltaR(const Particle* p) const {
  return DeltaR(p->eta(),p->phi());
}

floatingnumber Particle::DeltaR(const Particle p) const {
  return DeltaR(p.eta(),p.phi());
}

floatingnumber Particle::DeltaR(const Double_t eta, const Double_t phi) const {
  Double_t deta = *(m_eta) - eta;
  Double_t dphi = *(m_phi) - phi;
  double pi = TMath::Pi();
  double twopi = 2*pi;
  while(dphi >= pi) dphi -= twopi;
  while(dphi < -pi) dphi += twopi;
  return sqrt( deta*deta+dphi*dphi );
}

floatingnumber Particle::M(const Particle p) const {
  Double_t E2 = pow(*(m_e) + p.e(),2);
  Double_t P2 = pow(*(m_pt)*cosh(*(m_eta)),2) + pow(p.pt()*cosh(p.eta()),2)
                + 2*(*(m_pt))*p.pt()*(cos(*(m_phi)-p.phi())+sinh(*(m_eta))*sinh(p.eta()));
  if(E2<P2)
    return -sqrt( P2 - E2 );
  return sqrt( E2 - P2 );
}

ostream& operator<<( ostream& out, const Particle& rhs ) {
  out << " m:"   << rhs.m()
      << " e:"   << rhs.e()
      << " pt:"  << rhs.pt()
      << " eta:" << rhs.eta()
      << " phi:" << rhs.phi();
  return out;
}

Particle& Particle::operator*=(const floatingnumber scale) {
  *(m_e)  *= scale;
  *(m_m)  *= scale;
  *(m_pt) *= scale;
  return *this;
}

bool sortParticlePt::operator()( const Particle& p1, const Particle& p2 ) {
  return p1.pt() > p2.pt(); //( p1.pt() > p2.pt() ) ? true : false;
}

TLorentzVector* Particle::getTLV() const {
  TLorentzVector* tlv = new TLorentzVector();
  tlv->SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;
}

TLorentzVector Particle::tlv() const {
  TLorentzVector tlv;
  tlv.SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;
}
