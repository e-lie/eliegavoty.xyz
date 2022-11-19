import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--secondary', styles.heroBanner)}>
      <div className="container">
        {/* <h1 className="hero__title">{siteConfig.title}</h1> */}
        {/* <p className="hero__subtitle">{siteConfig.tagline}</p> */}
        <p className="hero__subtitle"><strong>Bonjour, je suis musicien, livecodeur, formateur et parfois philosophe des techniques.</strong></p>
        <p  className="hero__subtitle">Ce site, en cours d'élaboration, vise à rassembler <Link href='/docs/workshop'>des tutoriels de livecoding</Link> et des liens vers :</p>
        <p  className="hero__subtitle">...mon travail de musique livecodée sous le pseudo Jules Cipher >>>> 
        <Link
            className="button button--secondary button--lg"
            to='https://linktr.ee/julescipher'>
          https://linktr.ee/julescipher
        </Link>
        </p>
        <p  className="hero__subtitle">...et de philosophie, par exemple >>>>> <Link
            className="button button--secondary button--lg"
            to='https://reprogrammerboitenoi.re/'>
          https://reprogrammerboitenoi.re/
          </Link></p>
        <p  className="hero__subtitle">J'anime également un atelier de live/creative coding (FoxDot et hydra notamment) tous les mardi à à 19h >>> 
        <Link to='/docs/workshop'> plus d'informations ici</Link></p>
 
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Tutoriels&livecoding`}
      description="Tutoriels&livecoding"> 

      <HomepageHeader />
      <main>
        {/* <HomepageFeatures /> */}
      </main>
    </Layout>
  );
}
