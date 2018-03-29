# Blockchain Demo

## Demonstration

### Start Server

```bash
pip install -r requirements.txt
FLASK_APP=app.py flask run
```

### Make a transaction

```bash
curl "localhost:5000/txion" \
     -H "Content-Type: application/json" \
     -d '{"from": "abc", "to":"def", "amount": 3}'
```

### Mining

```bash
curl localhost:5000/mine
```

## Terms

**Gensis block**  [Link](https://en.bitcoin.it/wiki/Genesis_block)

> A genesis block is the first block of a block chain. Modern versions of Bitcoin number it as block 0, though very early versions counted it as block 1. The genesis block is almost always hardcoded into the software of the applications that utilize its block chain.

**Proof of work** [Link](https://en.bitcoin.it/wiki/Proof_of_work)

> A proof of work is a piece of data which is difficult (costly, time-consuming) to produce but easy for others to verify and which satisfies certain requirements. Producing a proof of work can be a random process with low probability so that a lot of trial and error is required on average before a valid proof of work is generated. Bitcoin uses the Hashcash proof of work system.

**consensus algorithm** [Link](http://whatis.techtarget.com/definition/consensus-algorithm)

> A consensus algorithm is a process in computer science used to achieve agreement on a single data value among distributed processes or systems. Consensus algorithms are designed to achieve reliability in a network involving multiple unreliable nodes. Solving that issue -- known as the consensus problem -- is important in distributed computing and multi-agent systems.

## Reference

- [Let’s Build the Tiniest Blockchain – Crypto Currently – Medium](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b)
- [Let’s Make the Tiniest Blockchain Bigger – Crypto Currently – Medium](https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d)
- [Blockchain Demo](https://anders.com/blockchain/blockchain.html)
- [A Hitchhiker’s Guide to Consensus Algorithms – Hacker Noon](https://hackernoon.com/a-hitchhikers-guide-to-consensus-algorithms-d81aae3eb0e3?gi=45c3596466a1)