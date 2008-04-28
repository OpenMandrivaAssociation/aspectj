# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define section free

Summary:        AspectJ aspect-oriented language extension to Java
Name:           aspectj
Version:        1.5.3
Release:        %mkrel 2.0.1
Epoch:          0
License:        Eclipse Public License
URL:            http://eclipse.org/aspectj/
Group:          Development/Java
Source0:        aspectj-1.5.3-src.tar.gz
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools/ login 
# cvs -d:pserver:anonymous@dev.eclipse.org:/cvsroot/tools/ export -r V1_5_3_final org.aspectj

Source1:        aspectj-build-build.xml
Source2:        aspectj-jdtcore4aspectj-build.xml
Source3:        http://archive.apache.org/dist/jakarta/bcel/source/bcel-5.1-src.zip
Source4:        aspectj-1.5.3-build-bcel.xml
Source5:        aspectj-1.5.3-script-aj
Source6:        aspectj-1.5.3-script-aj5
Source7:        aspectj-1.5.3-script-ajbrowser
Source8:        aspectj-1.5.3-script-ajc
Source9:        aspectj-1.5.3-script-ajdoc
Source10:       aspectjlib-1.5.3.pom
Source11:       aspectjrt-1.5.3.pom
Source12:       aspectjtools-1.5.3.pom
Source13:       aspectjweaver-1.5.3.pom


Patch0:         aspectj-1.5.3-bcel-builder-build_xml.patch
Patch1:         aspectj-1.5.3-PluginModel.patch
Patch2:         aspectj-1.5.3-PluginFragmentModel.patch
Patch3:         aspectj-1.5.3-PluginModelObject.patch
Patch4:         aspectj-1.5.3-PluginRegistryModel.patch
Patch5:         aspectj-1.5.3-PluginPrerequisiteModel.patch
Patch6:         aspectj-1.5.3-LibraryModel.patch
Patch7:         aspectj-1.5.3-ResourceTree.patch
Patch8:         aspectj-1.5.3-ProjectPreferences.patch
Patch9:         aspectj-1.5.3-Resource.patch
Patch10:        aspectj-1.5.3-File.patch
Patch11:        aspectj-1.5.3-Project.patch
Patch12:        aspectj-1.5.3-SaveManager.patch
Patch13:        aspectj-1.5.3-CharsetManager.patch
Patch14:        aspectj-1.5.3-Workspace.patch
Patch15:        aspectj-1.5.3-BlobStore.patch
Patch16:        aspectj-1.5.3-HistoryStore2.patch
Patch17:        aspectj-1.5.3-JavaCore.patch
Patch18:        aspectj-1.5.3-Factory.patch
Patch19:        aspectj-1.5.3-CompilationUnitResolver.patch
Patch20:        aspectj-1.5.3-CompilationUnitProblemFinder.patch

#Patch1:         aspectj-docs-build_xml.patch
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  junit
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
BuildRequires:  java-rpmbuild >= 0:1.4.2
BuildRequires:  eclipse-platform 
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-collections
BuildRequires:  jakarta-commons-digester
BuildRequires:  jakarta-commons-logging
BuildRequires:  regexp
BuildRequires:  saxon
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
BuildRequires:  jdiff
BuildRequires:  asm2
Requires:  jakarta-commons-beanutils
Requires:  jakarta-commons-collections
Requires:  jakarta-commons-digester
Requires:  jakarta-commons-logging
Requires:  regexp
Requires:  saxon
Requires:  xalan-j2
Requires:  xerces-j2
Requires:  xml-commons-apis
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
AspectJ is a seamless aspect-oriented language 
extension to Java(tm). It can be used to cleanly 
modularize the crosscutting structure of concerns 
such as exception handling, multi-object protocols, 
synchronization, performance optimizations, and 
resource sharing. When implemented in a 
non-aspect-oriented fashion, the code for these concerns 
typically becomes spread out across entire programs. 
AspectJ controls such code-tangling and makes the 
underlying concerns more apparent, making programs 
easier to develop and maintain. The project goal 
is to support the AspectJ compiler and core tools. 

%package eclipse-plugins
Summary:        Eclipse Plugins for %{name}
Group:          Development/Java
Requires:       %{name} = 0:%{version}
Requires:       eclipse-platform

%description eclipse-plugins
%{summary}.

%package installer
Summary:        Installer for %{name}
Group:          Development/Java

%description installer
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
%{summary}.

%package manual
Summary:        Docs for %{name}
Group:          Development/Java

%description manual
%{summary}.

%prep
%setup -q -n org.%{name}
cp %{SOURCE1} modules/build/build-build.xml
cp %{SOURCE3} modules/bcel-builder
cp %{SOURCE4} modules/bcel-builder/build-bcel.xml
#def##cp %{SOURCE3} modules/org.eclipse.jdt.core/jdtcore-for-aspectj-src.zip
#rap#touch modules/build/local.properties
#rap#rm modules/loadtime/src/org/aspectj/weaver/loadtime/JRockitAgent.java
cp %{SOURCE2} modules/org.eclipse.jdt.core/build.xml

# remove all binary libs
# bundled aspectjrt.jar and aspectjtools.jar are 0 byte, though required
find . -name "*.jar" -a ! -name "aspectj*.jar" -exec rm {} \;
#for j in $(find . -name "*.jar" -a ! -name "aspectj*.jar"); do
#       mv $j $j.no
#done
# next has been rebuilt from sources
# throw 4 jakarta-commons from JPP into one jar
( cd modules/lib/commons
  jar xf $(find-jar commons-beanutils)
  jar xf $(find-jar commons-collections)
  jar xf $(find-jar commons-digester)
  jar xf $(find-jar commons-logging)
  jar cf commons.jar org
)

ln -sf $(build-classpath ant) modules/lib/ant/lib/ant.jar
ln -sf $(build-classpath ant-launcher) modules/lib/ant/lib/ant-launcher.jar
ln -sf $(build-classpath ant/ant-junit) modules/lib/ant/lib/ant-junit.jar
ln -sf $(build-classpath ant/ant-nodeps) modules/lib/ant/lib/ant-nodeps.jar
ln -sf $(build-classpath xerces-j2) modules/lib/ant/lib/xercesImpl.jar
ln -sf $(build-classpath xml-commons-apis) modules/lib/ant/lib/xml-apis.jar
ln -sf $(build-classpath jdiff) modules/lib/jdiff/jdiff.jar
ln -sf $(build-classpath asm2/asm2) modules/lib/asm/asm-2.2.1.jar
ln -sf $(build-classpath junit) modules/lib/junit/junit.jar
ln -sf $(build-classpath regexp) modules/lib/regexp/jakarta-regexp-1.2.jar
ln -sf $(build-classpath saxon) modules/lib/saxon/saxon.jar

pushd modules/org.eclipse.jdt.core
  mkdir src
  cd src
  unzip -q ../jdtcore-for-aspectj-src.zip
  rm -rf javax
  rm -rf org/apache
  rm -rf org/w3c
  rm -rf org/xml
  cd ..
popd
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%patch12 -b .sav12
%patch13 -b .sav13
%patch14 -b .sav14
%patch15 -b .sav15
%patch16 -b .sav16
%patch17 -b .sav17
%patch18 -b .sav18
%patch19 -b .sav19
%patch20 -b .sav20

rm modules/loadtime/src/org/aspectj/weaver/loadtime/JRockitAgent.java

mv modules/build/build-properties.xml modules/build/build-properties.xml.orig
sed -e 's|"DEVELOPMENT"|"1.5.3"|' modules/build/build-properties.xml.orig \
     > modules/build/build-properties.xml

# Avoid use of eclipse's OperationCanceledException
for j in $(find . -name "*.java" -exec grep -l "org\.eclipse\.core\.runtime\.OperationCanceledException" {} \;); do
    sed -i -e '/import org\.eclipse\.core\.runtime\.OperationCanceledException/d' $j
    sed -i -e 's/org\.eclipse\.core\.runtime\.OperationCanceledException/org\.eclipse\.core\.runtime\.OperationCanceledException/' $j
    sed -i -e 's/OperationCanceledException/RuntimeException/g' $j
done

%build
export JAVA_HOME=%{_jvmdir}/java-rpmbuild
export ANT_OPTS="-Xmx384m"
# CLASSPATH needed for rebuilds from sources
#rap#export OPT_JAR_LIST="ant/ant-junit junit ant/ant-nodeps"
export CLASSPATH=$(build-classpath \
ant \
ant-launcher \
commons-logging \
)

# now for eclipse 3.2.X
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.osgi_*.jar)
#CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.osgi.util_*.jar)
#CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.jface.text_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.text_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.update.configurator_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.core.runtime_*.jar)
#rap#CLASSPATH=${CLASSPATH}:/usr/lib/jvm/java-1.4.2-bea/jre/lib/managementserver.jar
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.equinox.common_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.core.contenttype_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.equinox.preferences_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.equinox.registry_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_datadir}/eclipse/plugins/org.eclipse.core.jobs_*.jar)

# rebuild jdtcore-for-aspectj.jar from sources
pushd modules/org.eclipse.jdt.core
export ASPECTJ_HOME=$RPM_BUILD_DIR/org.aspectj/modules/lib/aspectj
"$JAVA_HOME/bin/java" -classpath "$ASPECTJ_HOME/lib/aspectjtools.jar:$ASPECTJ_HOME/lib/aspectjrt.jar:$JAVA_HOME/lib/tools.jar:$CLASSPATH" -Xmx384M org.aspectj.tools.ajc.Main -sourceroots src -d build-classes
%ant jar
popd

#cp modules/org.eclipse.jdt.core/jdtcore-for-aspectj.jar.no modules/org.eclipse.jdt.core/jdtcore-for-aspectj.jar 

pushd modules/bcel-builder
%ant -f build-bcel.xml
cp bin/bcel.jar .
%ant extractAndPatchAndJar
%ant push
popd

# rebuild the build-module from sources
pushd modules/build
%ant -f build-build.xml
# do the product build
touch local.properties
%ant -Dbuild.sysclasspath=first
# do the release build
%ant -f release/build.xml \
       -Dversion=%{version} -Dskip.cvs=true \
       -Daspectj.modules.dir=$(pwd)/.. \
       -Djava15.home=%{_jvmdir}/java-rpmbuild \
       -Drun.14.only=false \
       -Dmin.vm=15 \
       -Dmax.vm=15 \
       install \
    | tee build-log-release-aspectj-%{version}.txt
# do the test build
%ant -f release/build.xml \
       -Dversion=%{version} -Dskip.cvs=true \
       -Daspectj.modules.dir=$(pwd)/.. \
       -Djava15.home=%{_jvmdir}/java-rpmbuild \
       -Dskip.build=true \
       -Drun.14.only=false \
       -Dmin.vm=15 \
       -Dmax.vm=15 \
       product-tests \
    | tee test-log-release-aspectj-%{version}.txt
popd


%install
rm -rf $RPM_BUILD_ROOT
# jars, poms, depmap frags
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 0644 modules/aj-build/dist/tools/lib/aspectjlib.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}lib-%{version}.jar
install -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-aspectjlib.pom
%add_to_maven_depmap %{name} %{name}lib %{version} JPP %{name}lib
install -m 0644 modules/aj-build/dist/tools/lib/aspectjrt.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}rt-%{version}.jar
install -m 0644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-aspectjrt.pom
%add_to_maven_depmap %{name} %{name}rt %{version} JPP %{name}rt
install -m 0644 modules/aj-build/dist/tools/lib/aspectjtools.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}tools-%{version}.jar
install -m 0644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-aspectjtools.pom
%add_to_maven_depmap %{name} %{name}tools %{version} JPP %{name}tools
install -m 0644 modules/aj-build/dist/tools/lib/aspectjweaver.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}weaver-%{version}.jar
install -m 0644 %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-aspectjweaver.pom
%add_to_maven_depmap %{name} %{name}weaver %{version} JPP %{name}weaver
install -m 0644 modules/aj-build/dist/aspectj-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}installer-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# plugins
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/eclipse/plugins
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.ajde
cp -pr modules/aj-build/dist/ide/eclipse/org.aspectj.ajde/* $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.ajde
pushd $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.ajde
rm aspectjrt.jar
ln -sf ../../aspectjrt.jar .
rm aspectjtools.jar
ln -sf ../../aspectjtools.jar .
popd
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde $RPM_BUILD_ROOT%{_datadir}/eclipse/plugins/org.aspectj.ajde

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc
cp -pr modules/aj-build/dist/ide/eclipse/org.aspectj.ajde.doc/* $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc $RPM_BUILD_ROOT%{_datadir}/eclipse/plugins/org.aspectj.ajde.doc

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.ajde.source
cp -pr modules/aj-build/dist/ide/eclipse/org.aspectj.ajde.source/* $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.ajde.source
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde.source $RPM_BUILD_ROOT%{_datadir}/eclipse/plugins/org.aspectj.ajde.source

install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
cp -pr modules/aj-build/dist/ide/eclipse/org.aspectj.aspectjrt/* $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
pushd $RPM_BUILD_ROOT%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
rm aspectjrt.jar
ln -sf ../../aspectjrt.jar .
popd
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt $RPM_BUILD_ROOT%{_datadir}/eclipse/plugins/org.aspectj.aspecjrt

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr modules/aj-build/dist/docs/doc/runtime-api \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr modules/aj-build/dist/docs/doc/weaver-api \
        $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

rm -rf modules/aj-build/dist/docs/doc/runtime-api
rm -rf modules/aj-build/dist/docs/doc/weaver-api

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr modules/aj-build/dist/docs/* \
        $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}/runtime-api \
        $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}/weaver-api \
        $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# scripts
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -m 0755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/aj
install -m 0755 %{SOURCE6} $RPM_BUILD_ROOT%{_bindir}/aj5
install -m 0755 %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/ajbrowser
install -m 0755 %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/ajc
install -m 0755 %{SOURCE9} $RPM_BUILD_ROOT%{_bindir}/ajdoc

# home
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
ln -s %{_bindir}/aj $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/aj
ln -s %{_bindir}/aj5 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/aj5
ln -s %{_bindir}/ajbrowser $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/ajbrowser
ln -s %{_bindir}/ajc $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/ajc
ln -s %{_bindir}/ajdoc $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/ajdoc
ln -s %{_docdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
ln -s %{_javadir}/%{name}lib.jar \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/%{name}lib.jar
ln -s %{_javadir}/%{name}rt.jar \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/%{name}rt.jar
ln -s %{_javadir}/%{name}tools.jar \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/%{name}tools.jar
ln -s %{_javadir}/%{name}weaver.jar \
      $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/%{name}weaver.jar

%clean
rm -rf $RPM_BUILD_ROOT

%post eclipse-plugins
rm -f %{_datadir}/eclipse/plugins/org.aspectj.ajde
ln -s %{_javadir}/%{name}-eclipse/org.aspectj.ajde %{_datadir}/eclipse/plugins/org.aspectj.ajde
rm -f %{_datadir}/eclipse/plugins/org.aspectj.ajde.doc
ln -s %{_javadir}/%{name}-eclipse/org.aspectj.ajde.doc %{_datadir}/eclipse/plugins/org.aspectj.ajde.doc
rm -f %{_datadir}/eclipse/plugins/org.aspectj.ajde.source
ln -s %{_javadir}/%{name}-eclipse/org.aspectj.ajde.source %{_datadir}/eclipse/plugins/org.aspectj.ajde.source
rm -f %{_datadir}/eclipse/plugins/org.aspectj.aspectjrt
ln -s %{_javadir}/%{name}-eclipse/org.aspectj.aspectjrt %{_datadir}/eclipse/plugins/org.aspectj.aspectjrt

%postun eclipse-plugins
if [ "$1" = "0" ]; then
  rm -f %{_datadir}/eclipse/plugins/org.aspectj.ajde
  rm -f %{_datadir}/eclipse/plugins/org.aspectj.ajde.doc
  rm -f %{_datadir}/eclipse/plugins/org.aspectj.ajde.source
  rm -f %{_datadir}/eclipse/plugins/org.aspectj.aspectjrt
fi

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/*.html
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_javadir}/%{name}lib*.jar
%{_javadir}/%{name}rt*.jar
%{_javadir}/%{name}tools*.jar
%{_javadir}/%{name}weaver*.jar
%dir %{_datadir}/maven2/poms
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}

%files eclipse-plugins
%defattr(0644,root,root,0755)
%{_javadir}/aspectj-eclipse
%ghost %{_datadir}/eclipse/plugins/*

%files installer
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}/*.html
%{_javadir}/%{name}installer*.jar

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-%{version}


