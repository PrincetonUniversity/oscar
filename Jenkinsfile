node {
    dir('oscar') {
            credentialsId: '7b297dac-f7d7-4d5d-ad4f-cbf05b32e954',
            refspec: '+refs/pull/*:refs/remotes/origin/pr/*',
            git url: 'git@github.com:PrincetonUniversity/oscar.git',
            git branch: '${sha1}'
                
    }
    dir('oscar-exercises') {
            credentialsId: '0a2a1efd-124f-4e81-8127-3fe431958c0a',
            git url: 'git@github.com:PrincetonUniversity/oscar-exercises.git',
            git branch: 'master'
                
    }
    sh('. oscar/build-oscar.sh')
    sh('. oscar/build-exercises.sh')    
}
