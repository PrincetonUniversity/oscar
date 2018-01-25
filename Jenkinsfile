node {
    dir('oscar-dir') {
            credentialsId: '7b297dac-f7d7-4d5d-ad4f-cbf05b32e954',
            refspec: '+refs/pull/*:refs/remotes/origin/pr/*',
            git url: 'git@github.com:PrincetonUniversity/oscar.git',
            git branch: '${sha1}'
                
    }
    dir('oscar-exercises-dir') {
            credentialsId: '0a2a1efd-124f-4e81-8127-3fe431958c0a',
            git url: 'git@github.com:PrincetonUniversity/oscar-exercises.git',
            git branch: 'master'
                
    }
    sh('. oscar-dir/build-oscar.sh')
    sh('. oscar-dir/build-exercises.sh')    
}
