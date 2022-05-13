# Basic Concepts

- Written in Dec. 03. 2021
- Authored by Jaycol Kim <jaycol@gmail.com>

## Maven

### Artifact

- Artifact란 JAR과 같은 파일을 일컫는데, Maven 리포지토리에 배포되는 파일입니다. Maven 빌드는 하나 이상의 Artifact를 생성하는데, 컴파일된 JAR 과 소스 JAR과 같은 파일들을 생성합니다. 각각의 아티팩트는 `com.example.foo` 리버스 도메인 네임과 같은 그룹 ID, Artifact ID, 버전명 등을 가집니다. 그래서 프로젝트의 종속성 또한 Artifact에 의해 명시될 수 있습니다.

## Gradle

### Build phases

1. Initialization
1. Configuration
1. Execution

### File structures

```text
project-name/
    build.gradle
    settings.gradle
    src/
```

- `build.gradle`

```java

println '[2] This is executed during the configuration phase.'
 
task configured {
    println '[3] This is also executed during the configuration phase.'
}
 
task test1 << {
    println '[4] This is executed during the execution phase.'
}
 
task test2 {
    doFirst {
        println '[5] This is executed first during the execution phase.'
    }
    doLast {
        println '[6] This is executed last during the execution phase.'
    }
    println '[4] This is executed during the configuration phase as well.'
}

```

- `settings.gradle`

```java
println '[1] This is executed during the initialization phase.'
```

### Execution

- Execute test1

```bash
$ gradle test1
[1] This is executed during the initialization phase.
[2] This is executed during the configuration phase.
[3] This is also executed during the configuration phase.
[4] This is executed during the configuration phase as well.
:test1
[4] This is executed during the execution phase.

BUILD SUCCESSFUL

Total time: 0.832 secs
```

- Execute test2

```bash
$ gradle test2
[1] This is executed during the initialization phase.
[2] This is executed during the configuration phase.
[3] This is also executed during the configuration phase.
[4] This is executed during the configuration phase as well.
:test2
[5] This is executed first during the execution phase.
[6] This is executed last during the execution phase.

BUILD SUCCESSFUL

Total time: 0.812 secs
```
